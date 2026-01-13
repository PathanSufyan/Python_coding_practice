"""
Retail ETL Pipeline DAG
======================
This DAG orchestrates an ETL pipeline for retail customer analytics using Amazon EMR.
It includes robust error handling, retry logic, and secure data processing.
"""

from airflow import DAG
from airflow.providers.amazon.aws.operators.emr import (
    EmrCreateJobFlowOperator, 
    EmrAddStepsOperator, 
    EmrTerminateJobFlowOperator
)
from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.utils.email import send_email
from datetime import timedelta
import boto3
import json
import logging
from typing import Any, Dict, Optional, Union, Type


# ====== Error Handling & Notification Functions ====== #

def task_failure_alert(context):
    """
    Custom failure alert function for Airflow tasks.
    Logs detailed error and sends notifications via SNS and email.
    """
    # Extract context information
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    execution_date = context.get('execution_date')
    log_url = context.get('task_instance').log_url
    error = context.get('exception')
    
    # Format the failure message
    message = (f"❌ Airflow Task Failure Detected! \n\n"
               f"DAG: {dag_id}\n"
               f"Task: {task_id}\n"
               f"Execution Time: {execution_date}\n"
               f"Log URL: {log_url}\n"
               f"Error: {error}\n")
    
    # Log the detailed error
    logging.error(f"Task Failed! DAG: {dag_id}, Task: {task_id}, Error: {error}")
    
    # Send SNS notification
    try:
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")
        sns_client = boto3.client('sns', region_name='us-east-1')
        
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failed: {dag_id} - {task_id}",
            Message=message
        )
        logging.info(f"SNS notification sent! Message ID: {response['MessageId']}")
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")
    
    # Send email to support team
    try:
        send_email(
            to='your-team@example.com',
            subject=f"Task Failure: {dag_id} - {task_id}",
            html_content=f"Task {task_id} failed in DAG {dag_id} at {execution_date}.<br>Error: {error}<br>Log URL: {log_url}"
        )
    except Exception as email_error:
        logging.error(f"Failed to send email notification: {email_error}")


def log_to_cloudwatch(message: str) -> None:
    """
    Logs messages to AWS CloudWatch for external monitoring.
    """
    try:
        client = boto3.client('logs', region_name='us-east-1')
        log_group_name = "/aws/airflow/retail-etl"
        log_stream_name = "task-errors"
        
        # Put log events to CloudWatch
        client.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=[
                {
                    'timestamp': int(datetime.now().timestamp() * 1000),
                    'message': message
                }
            ]
        )
    except Exception as e:
        logging.error(f"Failed to log to CloudWatch: {str(e)}")


def retry_conditionally(context):
    """
    Implements conditional retry logic based on the exception type.
    Returns True to trigger a retry, False otherwise.
    """
    exception = context.get('exception')
    
    # Define which exceptions should trigger a retry
    if isinstance(exception, ConnectionError):
        logging.info("Retrying due to network error...")
        return True
    elif isinstance(exception, TimeoutError):
        logging.info("Retrying due to timeout...")
        return True
    elif "ServiceUnavailable" in str(exception):  # AWS service unavailable
        logging.info("Retrying due to AWS service unavailability...")
        return True
    else:
        logging.error(f"Non-retryable error encountered: {exception}")
        # Log to CloudWatch for serious errors
        log_to_cloudwatch(f"Non-retryable error in task {context.get('task_instance').task_id}: {exception}")
        return False


def emr_step_failure_alert(context):
    """
    Specific handler for EMR step failures with custom logic based on exception types.
    """
    exception = context.get('exception')
    task_id = context.get('task_instance').task_id
    
    # Handle specific EMR-related errors
    if isinstance(exception, ValueError):
        logging.error(f"EMR step {task_id} failed due to invalid configuration: {exception}")
    elif isinstance(exception, TimeoutError):
        logging.error(f"EMR step {task_id} failed due to timeout: {exception}")
    elif "ClusterTerminated" in str(exception):
        logging.error(f"EMR step {task_id} failed because cluster was terminated: {exception}")
    else:
        logging.error(f"EMR step {task_id} failed due to unknown error: {exception}")
    
    # Forward to the general failure handler
    task_failure_alert(context)


# ====== Helper Functions ====== #

def load_emr_config():
    """
    Loads EMR cluster configuration from a JSON file.
    """
    try:
        with open('/opt/airflow/dags/configs/emr_cluster_config.json', 'r') as f:
            config = json.load(f)
            
        # Ensure EBS encryption is enabled for data at rest
        if 'Instances' in config:
            if 'EbsConfiguration' not in config['Instances']:
                config['Instances']['EbsConfiguration'] = {
                    'EbsOptimized': True,
                    'EbsBlockDeviceConfigs': [
                        {
                            'VolumeSpecification': {
                                'SizeInGB': 100,
                                'VolumeType': 'gp2',
                                'Encrypted': True,
                            },
                            'VolumesPerInstance': 1,
                        }
                    ],
                }
            
        # Ensure SSL is enabled for data in transit
        if 'Configurations' not in config:
            config['Configurations'] = []
            
        found_core_site = False
        for conf in config['Configurations']:
            if conf.get('Classification') == 'core-site':
                conf['Properties']['hadoop.ssl.enabled'] = 'true'
                found_core_site = True
                break
                
        if not found_core_site:
            config['Configurations'].append({
                'Classification': 'core-site',
                'Properties': {
                    'hadoop.ssl.enabled': 'true',
                },
            })
            
        return config
    except Exception as e:
        logging.error(f"Failed to load EMR configuration: {e}")
        raise


def validate_data_quality(**kwargs):
    """
    Validates data quality by checking for the presence of processed files in S3.
    """
    try:
        client = boto3.client('s3')
        bucket = 'your-bucket'
        prefix = 'processed_data/'
        
        # List objects in the destination bucket
        response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        
        # Check if files exist
        if 'Contents' not in response:
            raise ValueError(f"Data quality check failed: No files found in {prefix}")
            
        files = [obj['Key'] for obj in response.get('Contents', [])]
        
        if not files:
            raise ValueError(f"Data quality check failed: No files found in {prefix}")
        else:
            file_count = len(files)
            logging.info(f"Data quality check passed: Found {file_count} files.")
            
            # Additional quality checks could be added here
            # For example, checking file sizes, schema validation, etc.
            
    except Exception as e:
        logging.error(f"Data quality validation failed: {e}")
        raise


def upload_to_s3_with_encryption(bucket_name: str, file_path: str, s3_key: str) -> None:
    """
    Uploads a file to S3 with server-side encryption enabled.
    """
    try:
        s3_client = boto3.client('s3')
        
        # Upload with AES256 encryption
        s3_client.upload_file(
            file_path, 
            bucket_name, 
            s3_key,
            ExtraArgs={'ServerSideEncryption': 'AES256'}
        )
        logging.info(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key} with encryption")
    except Exception as e:
        logging.error(f"Failed to upload file to S3: {e}")
        raise


# ====== DAG Definition ====== #

# Default arguments for all tasks
default_args = {
    'owner': 'retail-team',
    'depends_on_past': False,
    'email': ['your-team@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=60),
    'on_failure_callback': task_failure_alert,
}

# DAG definition
with DAG(
    'retail_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for Retail customer analytics with robust error handling',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['retail', 'aws', 'emr', 's3', 'airflow'],
) as dag:

    # Step 1: Create EMR Cluster
    create_emr_cluster = EmrCreateJobFlowOperator(
        task_id='create_emr_cluster',
        job_flow_overrides=load_emr_config(),
        aws_conn_id='aws_default',
        region_name='us-east-1',
        on_failure_callback=task_failure_alert,
        on_retry_callback=retry_conditionally,
    )

    # Step 2: Submit PySpark ETL Job
    add_steps = EmrAddStepsOperator(
        task_id='add_emr_steps',
        job_flow_id="{{ task_instance.xcom_pull(task_ids='create_emr_cluster', key='return_value') }}",
        aws_conn_id='aws_default',
        steps=[
            {
                'Name': 'retail_etl_job',
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': [
                        'spark-submit',
                        '--deploy-mode', 'cluster',
                        's3://your-bucket/emr_jobs/retail_etl_job.py',
                        '--source_path', 's3://your-bucket/raw_data/',
                        '--destination_path', 's3://your-bucket/processed_data/'
                    ],
                },
            }
        ],
        on_failure_callback=emr_step_failure_alert,
        on_retry_callback=retry_conditionally,
    )

    # Step 3: Monitor EMR Step Completion
    monitor_emr_step = EmrStepSensor(
        task_id='monitor_emr_step',
        job_flow_id="{{ task_instance.xcom_pull('create_emr_cluster', key='return_value') }}",
        step_id="{{ task_instance.xcom_pull(task_ids='add_emr_steps', key='return_value')[0] }}",
        aws_conn_id='aws_default',
        on_failure_callback=task_failure_alert,
        on_retry_callback=retry_conditionally,
    )

    # Step 4: Data Quality Check
    data_quality_check = PythonOperator(
        task_id='data_quality_check',
        python_callable=validate_data_quality,
        provide_context=True,
        on_failure_callback=task_failure_alert,
        on_retry_callback=retry_conditionally,
    )

    # Step 5: Terminate EMR Cluster
    terminate_emr_cluster = EmrTerminateJobFlowOperator(
        task_id='terminate_emr_cluster',
        job_flow_id="{{ task_instance.xcom_pull(task_ids='create_emr_cluster', key='return_value') }}",
        aws_conn_id='aws_default',
        trigger_rule='all_done',  # Terminate even if steps fail
        on_failure_callback=task_failure_alert,
    )

    # Step 6: Send Success Email
    send_success_email = EmailOperator(
        task_id='send_success_email',
        to='your-team@example.com',
        subject='Retail ETL Pipeline Succeeded',
        html_content="""
        <h3>ETL Pipeline Completed Successfully</h3>
        <p>The Retail ETL pipeline has completed all tasks successfully.</p>
        <p>You can access the processed data at: <code>s3://your-bucket/processed_data/</code></p>
        """,
        trigger_rule='all_success',
    )

    # Define the workflow
    create_emr_cluster >> add_steps >> monitor_emr_step >> data_quality_check >> terminate_emr_cluster >> send_success_email