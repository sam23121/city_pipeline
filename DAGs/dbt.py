from airflow import DAG
from airflow_dbt.operators.dbt_operator import DbtRunOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

#
# The default dir contains my dbt models, the retries has been added
# to handle if the cloud provider is offline for maintenance (this happened).
# Finally, I allow 30 minutes to attempt a re-execution of the DAG
#
default_args = {
    'dir': '/home/sam/Desktop/10_acad/week_11/data_warehouse/dbt/postgres_dwh1',
    'start_date': days_ago(0),                                               
}


with DAG(dag_id='transform_data', default_args=default_args) as dag:

    dbt_run = BashOperator(
        task_id='transform',
        bash_command='dbt run --projects_dir /home/sam/Desktop/10_acad/week_11/data_warehouse/dbt/postgres_dwh1',
        dag=dag
    )

    dbt_test = BashOperator(
        task_id='moving_average_calc',
        bash_command='dbt test --projects_dir /home/sam/Desktop/10_acad/week_11/data_warehouse/dbt/postgres_dwh1'
    )

    dbt_run >> dbt_test

