
from airflow import DAG
from airflow.providers.amazon.aws.operators.emr import EmrCreateJobFlowOperator, EmrAddStepsOperator, EmrTerminateJobFlowOperator
from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import boto3
import logging

# Default arguments applied to all tasks
default_args = {
    'owner': 'retail-team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'email': ['your-team@example.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'retail_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for Retail customer analytics',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['retail', 'aws', 'emr', 's3', 'airflow'],
) as dag:

    # Load EMR Cluster configuration
    def load_emr_config():
        import json
        with open('/opt/airflow/dags/configs/emr_cluster_config.json', 'r') as f:
            return json.load(f)
        
    emr_config = load_emr_config()

    # Step1: Create EMR Cluster
    create_emr_cluster = EmrCreateJobFlowOperator(
        task_id='create_emr_cluster',
        job_flow_overrides=emr_config,
        aws_conn_id='aws_default',
        region_name='us-east-1',
    )

    # Step2: Submit PySpark ETL Job
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
    )

    # Step3: Monitor EMR Step Completion
    monitor_emr_step = EmrStepSensor(
        task_id='monitor_emr_step',
        job_flow_id="{{ task_instance.xcom_pull('create_emr_cluster', key='return_value') }}",
        step_id="{{ task_instance.xcom_pull(task_ids='add_emr_steps', key='return_value')[0] }}",
        aws_conn_id='aws_default',
    )

    # Step4: Data Quality Check
    def validate_data_quality(**kwargs):
        client = boto3.client('s3')
        bucket = 'your-bucket'
        prefix = 'processed_data/'
        
        response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        
        if not files:
            raise ValueError(f"Data quality check failed: No files found in {prefix}")
        else:
            logging.info(f"Data quality check passed: Found {len(files)} files.")

    data_quality_check = PythonOperator(
        task_id='data_quality_check',
        python_callable=validate_data_quality,
        provide_context=True,
    )

    # Step5: Terminate EMR Cluster
    terminate_emr_cluster = EmrTerminateJobFlowOperator(
        task_id='terminate_emr_cluster',
        job_flow_id="{{ task_instance.xcom_pull(task_ids='create_emr_cluster', key='return_value') }}",
        aws_conn_id='aws_default',
        trigger_rule='all_done',   # Terminate even if steps fail
    )

    # Step6: Send Success Email
    send_success_email = EmailOperator(
        task_id='send_success_email',
        to='your-team@example.com',
        subject='Retail ETL Pipeline Succeeded',
        html_content='The Retail ETL pipeline completed successfully!',
        trigger_rule='all_success',
    )

    # Step7: Handle Failure Notifications (optional: you could SNS here too)
    # You can also add an SNSOperator if you want.

    # DAG dependencies
    create_emr_cluster >> add_steps >> monitor_emr_step >> data_quality_check >> terminate_emr_cluster >> send_success_email

import boto3
import logging
from airflow.models import Variable

def task_failure_alert(context):
    """
    Custom failure alert function for Airflow tasks.
    Sends a detailed failure message to an SNS topic or email.
    """

    # Gather task context
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
    
    logging.error(message)
    
    # Option 1: Send Email (Airflow can already send default emails too)
    # You can use EmailOperator if needed separately
    
    # Option 2: Publish to AWS SNS
    try:
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")  # Store your SNS topic ARN in Airflow Variables
        client = boto3.client('sns', region_name='us-east-1')
        
        response = client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failed: {dag_id} - {task_id}",
            Message=message
        )
        logging.info(f"SNS notification sent! Message ID: {response['MessageId']}")
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")

add_steps = EmrAddStepsOperator(
    task_id='add_emr_steps',
    on_failure_callback=task_failure_alert,
)



dag = DAG(
    'retail_etl_pipeline',
    default_args=default_args,
    description='Retail ETL with robust failure handling',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['retail', 'aws', 'airflow'],
    on_failure_callback=task_failure_alert,  # << GLOBAL FAILURE ALERT
)


def task_failure_alert(context):
    # Extracting the necessary info
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    execution_date = context.get('execution_date')
    log_url = context.get('task_instance').log_url
    error = context.get('exception')
    
    # Format failure message
    message = (f"❌ Airflow Task Failure Detected! \n\n"
               f"DAG: {dag_id}\n"
               f"Task: {task_id}\n"
               f"Execution Time: {execution_date}\n"
               f"Log URL: {log_url}\n"
               f"Error: {error}\n")
    
    # Publish to SNS
    try:
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")  # Fetch ARN from Airflow Variables
        client = boto3.client('sns', region_name='us-east-1')
        
        response = client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failed: {dag_id} - {task_id}",
            Message=message
        )
        logging.info(f"SNS notification sent! Message ID: {response['MessageId']}")
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")


#  Final DAG with SNS Failure Alerts
from airflow import DAG
from airflow.providers.amazon.aws.operators.emr import EmrCreateJobFlowOperator, EmrAddStepsOperator, EmrTerminateJobFlowOperator
from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import boto3
import logging
from airflow.models import Variable

# Failure handler function
def task_failure_alert(context):
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    execution_date = context.get('execution_date')
    log_url = context.get('task_instance').log_url
    error = context.get('exception')
    
    message = (f"❌ Airflow Task Failure Detected! \n\n"
               f"DAG: {dag_id}\n"
               f"Task: {task_id}\n"
               f"Execution Time: {execution_date}\n"
               f"Log URL: {log_url}\n"
               f"Error: {error}\n")
    
    try:
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")
        client = boto3.client('sns', region_name='us-east-1')
        
        response = client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failed: {dag_id} - {task_id}",
            Message=message
        )
        logging.info(f"SNS notification sent! Message ID: {response['MessageId']}")
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")

# DAG definition with the failure callback
default_args = {
    'owner': 'retail-team',
    'depends_on_past': False,
    'email_on_failure': True,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': task_failure_alert,  # Apply failure callback to all tasks
}

with DAG(
    'retail_etl_pipeline',
    default_args=default_args,
    description='Retail ETL with robust failure handling',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['retail', 'aws', 'airflow'],
) as dag:
    # Create and manage EMR tasks (same as previously discussed)

    # Example task
    create_emr_cluster = EmrCreateJobFlowOperator(
        task_id='create_emr_cluster',
        ...
    )

    create_emr_cluster.on_failure_callback = task_failure_alert  # Task-specific failure callback

    # Add dependencies and complete the DAG as usual



# Sample Task Failure Handler with Detailed Logging
import logging
from airflow.utils.email import send_email

def task_failure_alert(context):
    """
    Custom failure alert function for Airflow tasks.
    Logs detailed error and sends notifications.
    """
    
    # Extract the context information
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    execution_date = context.get('execution_date')
    log_url = context.get('task_instance').log_url
    error = context.get('exception')
    
    # Logging detailed error
    logging.error(f"Task Failed! DAG: {dag_id}, Task: {task_id}, Execution: {execution_date}, Error: {error}")
    
    # Optionally, log to a specific log group (e.g., CloudWatch or other systems)
    try:
        # Example of publishing failure details to SNS, or you can send emails etc.
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")
        sns_client = boto3.client('sns', region_name='us-east-1')
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failure - {dag_id} - {task_id}",
            Message=f"Task {task_id} failed at {execution_date}. Check logs at: {log_url}. Error: {error}"
        )
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")
    
    # Send an email directly to support team
    send_email(
        to='support@company.com',
        subject=f"Task Failure: {dag_id} - {task_id}",
        html_content=f"Task {task_id} failed in DAG {dag_id} at {execution_date}. Error: {error}. <br> Log URL: {log_url}"
    )


# Configuring Automatic Retries Based on Specific Failure Scenarios:
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow import DAG
import logging
import time

def my_etl_task(**kwargs):
    try:
        # Simulate ETL job
        logging.info("Starting ETL job...")
        # Simulate error (for demo purposes)
        raise ConnectionError("Temporary network issue.")
    except Exception as e:
        logging.error(f"Task failed due to error: {str(e)}")
        raise

def retry_conditionally(context):
    """
    Retry based on the specific exception type (e.g., ConnectionError)
    """
    exception = context.get('exception')
    if isinstance(exception, ConnectionError):  # Check for network issues
        logging.info("Retrying due to network error...")
        return True  # Return True to trigger a retry
    else:
        logging.error("Non-retryable error encountered.")
        return False  # Don't retry for other errors

# DAG definition with retries
default_args = {
    'owner': 'airflow',
    'retries': 3,  # Retry 3 times
    'retry_delay': timedelta(minutes=10),  # Wait for 10 minutes before retry
    'on_failure_callback': task_failure_alert,
    'retry_exponential_backoff': True,  # Exponential backoff (increase delay each retry)
    'max_retry_delay': timedelta(minutes=60),  # Max retry delay to avoid long wait times
}

dag = DAG(
    'conditional_retry_example',
    default_args=default_args,
    description='DAG with conditional retries',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=my_etl_task,
    provide_context=True,
    retries=3,
    retry_delay=timedelta(minutes=5),  # 5 minutes between retries
    on_failure_callback=task_failure_alert,
    dag=dag,
)

# You can add conditional retries based on the error type
etl_task.on_failure_callback = retry_conditionally


# Handling Specific Errors and Retries in Different Task Types

from airflow.providers.amazon.aws.operators.emr import EmrAddStepsOperator

def emr_step_task(**kwargs):
    # Simulating an EMR step job
    try:
        logging.info("Starting EMR job...")
        # Simulate error (for demo purposes)
        raise ValueError("Invalid job configuration.")
    except Exception as e:
        logging.error(f"EMR step failed: {str(e)}")
        raise

emr_task = EmrAddStepsOperator(
    task_id='add_emr_steps',
    job_flow_id='j-XYZ',
    steps=[
        # Define EMR steps here
    ],
    on_failure_callback=task_failure_alert,  # Use the same failure handler
    retries=3,  # Retry the EMR step 3 times
    retry_delay=timedelta(minutes=10),  # Retry after 10 minutes
    dag=dag
)

# Conditional retry for EMR task
emr_task.on_failure_callback = retry_conditionally


# Example of Logging and Retry in a More Complex DAG with Multiple Tasks:

with DAG(
    'complex_etl_pipeline',
    default_args=default_args,
    description='Complex ETL Pipeline with retries and logging',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['etl', 'retry', 'logging'],
) as dag:

    start_task = PythonOperator(
        task_id='start_task',
        python_callable=my_etl_task,
        retries=3,
        retry_delay=timedelta(minutes=5),
        on_failure_callback=task_failure_alert,
        dag=dag,
    )

    emr_step_task = EmrAddStepsOperator(
        task_id='emr_step_task',
        job_flow_id='j-XYZ',
        steps=[...],  # Add steps here
        retries=2,
        retry_delay=timedelta(minutes=10),
        on_failure_callback=task_failure_alert,
        dag=dag,
    )

    start_task >> emr_step_task


# Failure Callback for Task Failures:
def task_failure_alert(context):
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    execution_date = context.get('execution_date')
    log_url = context.get('task_instance').log_url
    error = context.get('exception')
    
    # Logging detailed error
    logging.error(f"Task Failed! DAG: {dag_id}, Task: {task_id}, Execution: {execution_date}, Error: {error}")
    
    # Sending notifications (SNS/email)
    try:
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")
        sns_client = boto3.client('sns', region_name='us-east-1')
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failure - {dag_id} - {task_id}",
            Message=f"Task {task_id} failed at {execution_date}. Check logs at: {log_url}. Error: {error}"
        )
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")
    
    # Send email to support team
    send_email(
        to='support@company.com',
        subject=f"Task Failure: {dag_id} - {task_id}",
        html_content=f"Task {task_id} failed in DAG {dag_id} at {execution_date}. Error: {error}. <br> Log URL: {log_url}"
    )


# Retries and Exponential Backoff:
default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': task_failure_alert,
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=60),
}


# Conditional Retry Logic:
def retry_conditionally(context):
    exception = context.get('exception')
    if isinstance(exception, ConnectionError):
        logging.info("Retrying due to network error...")
        return True  # Return True to trigger a retry
    else:
        logging.error("Non-retryable error encountered.")
        return False  # Don't retry for other errors


# Granular Error Handling for Specific Task Failures
def emr_step_failure_alert(context):
    exception = context.get('exception')
    if isinstance(exception, ValueError):
        logging.error(f"EMR step failed due to invalid configuration: {exception}")
        # Handle ValueError specifically
    elif isinstance(exception, TimeoutError):
        logging.error(f"EMR step failed due to timeout: {exception}")
        # Handle TimeoutError specifically
    else:
        logging.error(f"EMR step failed due to unknown error: {exception}")
    # Continue with the failure callback to notify the team
    task_failure_alert(context)


# Failure and Retry Logic in Task-Specific Operators
emr_add_steps_task = EmrAddStepsOperator(
    task_id='emr_add_steps',
    job_flow_id='j-XYZ',
    steps=[...],
    retries=2,  # Set retries per task
    retry_delay=timedelta(minutes=10),
    on_failure_callback=task_failure_alert,  # Common failure alert callback
    on_retry_callback=retry_conditionally,  # Retry only on specific conditions
    dag=dag
)


# Custom Retry Logic for Different Task Types
def retry_logic_for_s3_to_emr_task(context):
    exception = context.get('exception')
    if isinstance(exception, TimeoutError):
        # Retry S3 -> EMR tasks on timeout
        return True
    return False

s3_to_emr_task = PythonOperator(
    task_id='s3_to_emr_task',
    python_callable=transfer_data_to_emr,
    retries=5,
    retry_delay=timedelta(minutes=5),
    on_failure_callback=task_failure_alert,
    on_retry_callback=retry_logic_for_s3_to_emr_task,
    dag=dag
)


# Custom Failure Callback Function
import logging
import boto3
from airflow.utils.email import send_email
from airflow.models import Variable
from datetime import datetime

def task_failure_alert(context):
    """
    Custom failure alert function for Airflow tasks.
    Logs detailed error and sends notifications (SNS, email).
    """
    
    # Extract the context information
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    execution_date = context.get('execution_date')
    log_url = context.get('task_instance').log_url
    error = context.get('exception')
    
    # Logging detailed error
    logging.error(f"Task Failed! DAG: {dag_id}, Task: {task_id}, Execution: {execution_date}, Error: {error}")
    
    # Optionally, log to a specific log group (e.g., CloudWatch or other systems)
    try:
        sns_topic_arn = Variable.get("SNS_ALERT_TOPIC_ARN")
        sns_client = boto3.client('sns', region_name='us-east-1')
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Airflow Task Failure - {dag_id} - {task_id}",
            Message=f"Task {task_id} failed at {execution_date}. Check logs at: {log_url}. Error: {error}"
        )
    except Exception as sns_error:
        logging.error(f"Failed to send SNS notification: {sns_error}")
    
    # Send email to support team
    send_email(
        to='support@company.com',
        subject=f"Task Failure: {dag_id} - {task_id}",
        html_content=f"Task {task_id} failed in DAG {dag_id} at {execution_date}. Error: {error}. <br> Log URL: {log_url}"
    )


# Conditional Retry Logic for Specific Failure Types
def retry_conditionally(context):
    """
    Retry based on specific exception types, such as ConnectionError.
    """
    exception = context.get('exception')
    if isinstance(exception, ConnectionError):
        logging.info("Retrying due to network error...")
        return True  # Retry on ConnectionError
    elif isinstance(exception, TimeoutError):
        logging.info("Retrying due to timeout...")
        return True  # Retry on TimeoutError
    else:
        logging.error(f"Non-retryable error encountered: {exception}")
        return False  # Don't retry for other errors


# Task-Specific Retry Logic
from airflow.providers.amazon.aws.operators.emr import EmrAddStepsOperator
from airflow.operators.python import PythonOperator

def my_etl_task(**kwargs):
    try:
        logging.info("Starting ETL job...")
        # Simulate an error (for demo purposes)
        raise ConnectionError("Temporary network issue.")
    except Exception as e:
        logging.error(f"Task failed due to error: {str(e)}")
        raise

def emr_step_failure_alert(context):
    """
    Handle EMR step failures with custom logic based on exception types.
    """
    exception = context.get('exception')
    if isinstance(exception, ValueError):
        logging.error(f"EMR step failed due to invalid configuration: {exception}")
    elif isinstance(exception, TimeoutError):
        logging.error(f"EMR step failed due to timeout: {exception}")
    else:
        logging.error(f"EMR step failed due to unknown error: {exception}")
    task_failure_alert(context)

# Default args for retries and failure handling
default_args = {
    'owner': 'airflow',
    'retries': 3,  # Retry 3 times
    'retry_delay': timedelta(minutes=5),  # Retry after 5 minutes
    'on_failure_callback': task_failure_alert,
    'retry_exponential_backoff': True,  # Exponential backoff for retries
    'max_retry_delay': timedelta(minutes=60),
}

dag = DAG(
    'conditional_retry_etl',
    default_args=default_args,
    description='ETL DAG with retries and error handling',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['etl', 'retry', 'error-handling'],
)

# Example of task with retry on network error
etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=my_etl_task,
    retries=5,
    retry_delay=timedelta(minutes=10),
    on_failure_callback=task_failure_alert,
    on_retry_callback=retry_conditionally,  # Retry logic based on error
    dag=dag,
)

# Example of an EMR step with failure handling
emr_step_task = EmrAddStepsOperator(
    task_id='emr_step_task',
    job_flow_id='j-XYZ',
    steps=[...],  # Define steps for EMR
    retries=3,  # Retry 3 times
    retry_delay=timedelta(minutes=10),
    on_failure_callback=emr_step_failure_alert,  # Custom failure handler
    on_retry_callback=retry_conditionally,
    dag=dag,
)

etl_task >> emr_step_task


# Logging to External Systems (Optional but Recommended)
import boto3
import logging

def log_to_cloudwatch(message):
    try:
        client = boto3.client('logs', region_name='us-east-1')
        log_group_name = "/aws/airflow/logs"
        log_stream_name = "task-errors"
        
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

# Usage in failure callback
def task_failure_alert_with_cloudwatch(context):
    exception = context.get('exception')
    error_message = f"Task {context['task_instance'].task_id} failed: {str(exception)}"
    log_to_cloudwatch(error_message)
    task_failure_alert(context)  # Send email/SNS as usual


# Full DAG with Error Handling and Retry Logic
default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': task_failure_alert_with_cloudwatch,  # Updated with CloudWatch logging
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=60),
}

dag = DAG(
    'full_etl_pipeline',
    default_args=default_args,
    description='ETL DAG with retries, logging, and error handling',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['etl', 'retry', 'error-handling'],
)

etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=my_etl_task,
    retries=5,
    retry_delay=timedelta(minutes=10),
    on_failure_callback=task_failure_alert_with_cloudwatch,
    on_retry_callback=retry_conditionally,
    dag=dag,
)

emr_step_task = EmrAddStepsOperator(
    task_id='emr_step_task',
    job_flow_id='j-XYZ',
    steps=[...],  # Add your EMR steps here
    retries=3,
    retry_delay=timedelta(minutes=10),
    on_failure_callback=emr_step_failure_alert,
    on_retry_callback=retry_conditionally,
    dag=dag,
)

etl_task >> emr_step_task


default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': task_failure_alert_with_cloudwatch,  # Updated with CloudWatch logging
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=60),
}

dag = DAG(
    'full_etl_pipeline',
    default_args=default_args,
    description='ETL DAG with retries, logging, and error handling',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['etl', 'retry', 'error-handling'],
)

etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=my_etl_task,
    retries=5,
    retry_delay=timedelta(minutes=10),
    on_failure_callback=task_failure_alert_with_cloudwatch,
    on_retry_callback=retry_conditionally,
    dag=dag,
)

emr_step_task = EmrAddStepsOperator(
    task_id='emr_step_task',
    job_flow_id='j-XYZ',
    steps=[...],  # Add your EMR steps here
    retries=3,
    retry_delay=timedelta(minutes=10),
    on_failure_callback=emr_step_failure_alert,
    on_retry_callback=retry_conditionally,
    dag=dag,
)

etl_task >> emr_step_task


#  Encrypting Data in AWS S3
import boto3
from airflow.providers.amazon.aws.transfers.s3_to_s3 import S3ToS3Operator

def upload_to_s3_with_encryption(bucket_name, file_name):
    s3_client = boto3.client('s3')

    # Upload file to S3 with encryption enabled
    s3_client.upload_file(
        file_name, 
        bucket_name, 
        file_name,
        ExtraArgs={'ServerSideEncryption': 'AES256'}  # Use AES256 encryption
    )
s3_client.upload_file(
    file_name,
    bucket_name,
    file_name,
    ExtraArgs={
        'ServerSideEncryption': 'aws:kms', 
        'SSEKMSKeyId': 'your-kms-key-id'  # Use KMS encryption
    }
)


# Encrypting Data in Transit
from airflow.providers.amazon.aws.operators.emr import EmrCreateJobFlowOperator

cluster_config = {
    'Name': 'secure-emr-cluster',
    'LogUri': 's3://your-log-bucket/',
    'ReleaseLabel': 'emr-6.2.0',
    'Instances': {
        'InstanceGroups': [
            {
                'Name': 'Master',
                'Market': 'ON_DEMAND',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1,
            },
        ],
    },
    'Applications': [
        {'Name': 'Hadoop'},
        {'Name': 'Spark'},
    ],
    'Configurations': [
        {
            'Classification': 'core-site',
            'Properties': {
                'hadoop.ssl.enabled': 'true',  # Enable SSL for Hadoop
            },
        },
    ],
}

create_emr_cluster = EmrCreateJobFlowOperator(
    task_id='create_emr_cluster',
    job_flow_overrides=cluster_config,
    aws_conn_id='aws_default',
    region_name='us-east-1',
    dag=dag,
)


# Encrypting Data at Rest in EMR
from airflow.providers.amazon.aws.operators.emr import EmrCreateJobFlowOperator

cluster_config = {
    'Name': 'secure-emr-cluster',
    'LogUri': 's3://your-log-bucket/',
    'ReleaseLabel': 'emr-6.2.0',
    'Instances': {
        'InstanceGroups': [
            {
                'Name': 'Master',
                'Market': 'ON_DEMAND',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1,
            },
        ],
        'EbsConfiguration': {
            'EbsOptimized': True,
            'EbsBlockDeviceConfigs': [
                {
                    'VolumeSpecification': {
                        'SizeInGB': 100,
                        'VolumeType': 'gp2',
                        'Encrypted': True,  # Encrypt EBS volumes
                    },
                    'VolumesPerInstance': 1,
                }
            ],
        }
    },
    'Applications': [
        {'Name': 'Hadoop'},
        {'Name': 'Spark'},
    ],
}

create_emr_cluster = EmrCreateJobFlowOperator(
    task_id='create_encrypted_emr_cluster',
    job_flow_overrides=cluster_config,
    aws_conn_id='aws_default',
    region_name='us-east-1',
    dag=dag,
)
