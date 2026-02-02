import os 
import mlflow

from mlflow.tracking import MlflowClient

ENV = os.getenv('ENV')

mlflow.set_tracking_uri(os.getenv('MLFLOW_SERVER'))

class Model():
    
    def __init__(self):
        self.model = None
        self.transform_pipeline = None
        self.load_model()

    def load_model(self):
        client = MlflowClient()
        model_version = client.get_latest_versions(os.getenv("MLFLOW_REGISTRY_NAME"), ["ENV"])[]
        pipeline_path = 