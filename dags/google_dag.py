from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from tools.main import extract_google, letter_count, extract_spotify
from common_args import default_args

import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

with DAG(
    'google_imports',               #social_networks_imports
    default_args=default_args,
    description='DAG para importar datos de RS',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(8),
    tags=['aca va el tag'],
    catchup=False
) as dag:

    extract_google_task = PythonOperator(
        task_id='run_extraction_process',
        python_callable=extract_google,
        dag=dag,
    )

    extract_spotify_task = PythonOperator(
        task_id='run_extraction_process',
        python_callable=extract_spotify,
        dag=dag,
    )

    transform = PythonOperator(
        task_id='run_transformation_process',
        python_callable=letter_count,
        op_kwargs={'file_name':'data_source.csv','API_name':'google'},
        dag=dag,
    )

    extract >> transform
