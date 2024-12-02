import dagshub
dagshub.init(repo_owner='Namanfg', repo_name='End-to-End-DS-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)