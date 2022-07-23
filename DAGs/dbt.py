from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'start_date': days_ago(0), 
    'email_on_failure': True,
	'email': ['smlalene@gmail.com'],                                              
}


with DAG(dag_id='transform_data', default_args=default_args) as dag:

    dbt_run = BashOperator(
        task_id='transform',
        bash_command='dbt run --projects_dir ~/Desktop/10_acad/week_11/data_warehouse/dbt/postgres_dwh1',
        dag=dag
    )

    dbt_test = BashOperator(
        task_id='moving_average_calc',
        bash_command='dbt test --projects_dir ~/Desktop/10_acad/week_11/data_warehouse/dbt/postgres_dwh1'
    )

    dbt_run >> dbt_test

