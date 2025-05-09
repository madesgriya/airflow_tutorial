from airflow import DAG
from airflow.operators.bash import BashOperator 
from datetime import datetime, timedelta

default_args = {
    'owner': 'matty',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="sample",
    default_args=default_args,
    description="first dag",
    start_date=datetime(2025,5,9,15),
    schedule="@daily"
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world'
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="task2, run after task1"
    )
    
    task3 = BashOperator(
        task_id="third_task",
        bash_command="task3, run after task1 and in parallel to task2"
    )

    task1 >> [task2,task3]