from datetime import timedelta

default_args = {
        'owner': 'LucioSuppo',
        'depends_on_past': False,
        'email':['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
}
