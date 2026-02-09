import pandas as pd
import requests

dataset = pd.read_csv("data_test/primary.csv")
dataset = dataset.drop(["user_session", "user_id", "purchased"], axis=1)

rep = requests.post("https://purchase-predict-api-2-526969011890.europe-west9.run.app/predict", json=dataset.sample(n=10).to_json()).json()

print(rep)