# How to install airflow using docker
ensure you have your docker daemon and docker-compose running 

## Using Airflow `docker-compose.yaml`
follow the instruction on this link: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
* change the executor `CeleryExecutor` to `Local Executor`
* delete the redis, airflow-worker, and flower dependencies on the yaml file. 

## using AWS MWAA Local Runner
Clone this repository to your local repository:
```sh
git clone https://github.com/aws/aws-mwaa-local-runner.git  
```
after that, navigate to `aws-mwaa-local-runner` and follow the instruction from the `README.md` file.