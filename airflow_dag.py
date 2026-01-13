# from airflow import DAG
# from airflow.providers.amazon.aws.operators.emr_create_job_flow import EmrCreateJobFlowOperator
# from airflow.providers.amazon.aws.operators.emr_add_steps import EmrAddStepsOperator
# from airflow.providers.amazon.aws.sensors.emr_step import EmrStepSensor
# from airflow.providers.amazon.aws.operators.emr_terminate_job_flow import EmrTerminateJobFlowOperator
# from airflow.utils.dates import days_ago
# from airflow.operators.email import EmailOperator
# from airflow.providers.amazon.aws.operators.sns import SnsPublishOperator
# from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor




# default_args = {
#     'owner': 'retail_team',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'retries': 3,
#     'retry_delay': timedelta(minutes=5),
# }

# with DAG(
#     'retail_analytics_pipeline',
#     default_args=default_args,
#     description='Retail ETL with S3, EMR, and Airflow',
#     schedule_interval='@daily',
#     start_date=days_ago(1),
#     catchup=False,
# ) as dag:

#     create_emr_cluster = EmrCreateJobFlowOperator(
#         task_id='create_emr_cluster',
#         job_flow_overrides=JOB_FLOW_OVERRIDES,  # Define EMR config separately
#         aws_conn_id='aws_default',
#     )

#     add_steps = EmrAddStepsOperator(
#         task_id='add_steps',
#         job_flow_id="{{ task_instance.xcom_pull('create_emr_cluster', key='return_value') }}",
#         steps=SPARK_STEPS,  # Define your Spark ETL step separately
#         aws_conn_id='aws_default',
#     )

#     watch_step = EmrStepSensor(
#         task_id='watch_step',
#         job_flow_id="{{ task_instance.xcom_pull('create_emr_cluster', key='return_value') }}",
#         step_id="{{ task_instance.xcom_pull('add_steps', key='return_value')[0] }}",
#         aws_conn_id='aws_default',
#     )

#     terminate_emr_cluster = EmrTerminateJobFlowOperator(
#         task_id='terminate_emr_cluster',
#         job_flow_id="{{ task_instance.xcom_pull('create_emr_cluster', key='return_value') }}",
#         aws_conn_id='aws_default',
#         trigger_rule='all_done',  # terminate cluster even if step fails
#     )


# success_email = EmailOperator(
#     task_id='send_success_email',
#     to='your_email@example.com',
#     subject='Retail Analytics Pipeline Success',
#     html_content='<h3>The ETL pipeline has completed successfully!</h3>',
# )

# failure_email = EmailOperator(
#     task_id='send_failure_email',
#     to='your_email@example.com',
#     subject='Retail Analytics Pipeline Failed',
#     html_content='<h3>The ETL pipeline failed! Please check logs.</h3>',
#     trigger_rule='one_failed',  # This will trigger only if previous tasks fail
# )


# sns_success = SnsPublishOperator(
#     task_id="sns_success_notification",
#     target_arn="arn:aws:sns:your-region:your-account-id:your-sns-topic",
#     message="Retail Analytics ETL completed successfully!",
#     subject="SUCCESS: Retail Analytics Pipeline",
#     aws_conn_id="aws_default",
# )

# sns_failure = SnsPublishOperator(
#     task_id="sns_failure_notification",
#     target_arn="arn:aws:sns:your-region:your-account-id:your-sns-topic",
#     message="Retail Analytics ETL failed! Immediate attention needed.",
#     subject="FAILURE: Retail Analytics Pipeline",
#     aws_conn_id="aws_default",
#     trigger_rule="one_failed",
# )


# wait_for_step = EmrStepSensor(
#     task_id="watch_emr_step",
#     job_flow_id="{{ task_instance.xcom_pull(task_ids='create_emr_cluster') }}",
#     step_id="{{ task_instance.xcom_pull(task_ids='add_step') }}",
#     aws_conn_id="aws_default",
# )


# validate_data_quality = PythonOperator(
#     task_id='validate_data',
#     python_callable=validate_data_function,
# )

# create_emr_cluster >> add_steps >> watch_step >> terminate_emr_cluster >> success_email
# [create_emr_cluster, add_steps, watch_step, terminate_emr_cluster] >> failure_email


# execution_date = "{{ ds }}"  # Airflow's execution date (YYYY-MM-DD)
# year, month, day = execution_date.split('-')
# dynamic_path = f"s3://retail-analytics-project/raw/{year}/{month}/{day}/"
