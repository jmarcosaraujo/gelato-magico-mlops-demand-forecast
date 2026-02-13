from fastapi import FastAPI
import mlflow.sklearn
import pandas as pd
from src.config import MODEL_PATH

app = FastAPI(title="Gelato Mágico API")

model = mlflow.sklearn.load_model(MODEL_PATH)

@app.post("/predict")
def predict(temperatura: float):
    input_df = pd.DataFrame([[temperatura]], columns=["temperatura"])
    prediction = model.predict(input_df)
    return {"vendas_previstas": float(prediction[0])}
