import airflow.utils.dates
from airflow.models import DAG, PostgresOperator
dag = DAG(
   dag_id="extract",
   schedule_interval="",
   start_date=airflow.utils.dates.days_ago(1),
   catchup=False,
)

extract_data = PostgresOperator(
    dag=dag,
    task_id="extract_data",
    sql="../scripts/sql/unload.sql",
    postgres_conn_id="postgres_default",
    params={"traffic": "../data/20181029_d1_0800_0830.csv"},
    depends_on_past=True,
    wait_for_downstream=True,
)