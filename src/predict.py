import mlflow.sklearn
import pandas as pd
from src.config import MODEL_PATH

def predict(temperatura: float):
    model = mlflow.sklearn.load_model(MODEL_PATH)
    input_df = pd.DataFrame([[temperatura]], columns=["temperatura"])
    return model.predict(input_df)[0]
