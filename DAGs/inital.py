import airflow.utils.dates
from airflow.models import DAG
dag = DAG(
   dag_id="extract",
   schedule_interval="",
   start_date=airflow.utils.dates.days_ago(1),
   catchup=False,
)