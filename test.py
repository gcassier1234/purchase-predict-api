import pandas as pd
import requests

dataset = pd.read_csv("data_test/primary.csv")
dataset = dataset.drop(["user_session", "user_id", "purchased"], axis=1)

rep = requests.post("http://34.22.155.184/predict", json=dataset.sample(n=10).to_json()).json()

print(rep)