from datetime import datetime
import uuid

from airflow.models import DAG 
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

with DAG(dag_id='global_uuid',
         schedule_interval='@daily',
         start_date=...) as dag:

    generate_uuid = PythonOperator(
        task_id='generate_uuid',
        python_callable=lambda: str(uuid.uuid4())
    )

    print_uuid1 = BashOperator(
        task_id='print1',
        bash_command='echo {{ task_instance.xcom_pull("generate_uuid") }}'
    )

    print_uuid2 = BashOperator(
        task_id='print2',
        bash_command='echo {{ task_instance.xcom_pull("generate_uuid") }}'
    )

    generate_uuid >> print_uuid1 >> print_uuid2

