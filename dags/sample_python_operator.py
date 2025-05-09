from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'matty',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def print_hello():
    print("hello world")

with DAG(
    default_args = default_args,
    dag_id = "python_dag",
    description = "first python dag",
    start_date = datetime(2025,5,9,14),
    schedule = "@daily"
) as dag:
    task1 = PythonOperator(
        task_id="first_python_task",
        python_callable=,
        # execution_timeout=timedelta(hours=1)

    )