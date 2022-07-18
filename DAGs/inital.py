import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.postgres_operator import PostgresOperator

args = {'owner': 'airflow'}

dag = DAG(
   dag_id="extract",
   default_args=args,
   schedule_interval=None,
   start_date=airflow.utils.dates.days_ago(1),
   catchup=False,
)

extract_data = PostgresOperator(
    dag=dag,
    task_id="extract_data",
    sql="../scripts/sql/unload.sql",
    # postgres_conn_id = "postgres_local",
    postgres_conn_id="postgres_default",
    params={"traffic": "../data/20181029_d1_0800_0830.csv"},
    depends_on_past=True,
    wait_for_downstream=True,
)

extract_data

if __name__ == "__main__":
        dag.cli()