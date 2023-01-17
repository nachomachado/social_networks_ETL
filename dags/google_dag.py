from datetime import timedelta
from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from tools.main import extract
from common_args import default_args

with DAG(
    'google_imports',
    default_args=default_args,
    description='DAG para importar datos de google',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(8),
    tags=['aca va el tag'],
    catchup=False
) as dag:

    extraction = PythonOperator(
        task_id='run_exstraction_process',
        python_callable=extract,
        dag=dag,
    )

extraction