import os 
import joblib
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
        print(f"connecting to mlflow server: {os.getenv('MLFLOW_SERVER')}")
        print("eeeeeeeeeeeeeeeeeeeeee")
        print("eeeeeeeeeeeeeeeeeeeeee")
        print("eeeeeeeeeeeeeeeeeeeeee")
        experiments = client.search_experiments()
        model_version = client.get_model_version_by_alias(name=os.getenv("MLFLOW_REGISTRY_NAME"), alias="staging")
        pipeline_path = client.download_artifacts(model_version.run_id, "transform_pipeline.pkl")
        self.model = mlflow.sklearn.load_model("runs:/{}/model".format(model_version.run_id))

        self.transform_pipeline = joblib.load(pipeline_path)

    def predict(self, X):
        if self.model:
            if self.transform_pipeline:
                for name, encoder in self.transform_pipeline:
                    X[name] = X[name].fillna("unknown")
                    X[name] = encoder.transform(X[name])
            for col in ["user_id", "user_session", "purchased"]:
                if col in X:
                    X = X.drop(col, axis=1)
            return self.model.predict(X)
        return None