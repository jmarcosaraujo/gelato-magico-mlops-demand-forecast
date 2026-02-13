import mlflow.sklearn
from sklearn.metrics import r2_score, mean_squared_error
from src.preprocess import load_data, split_features_target
from src.config import DATA_PATH, MODEL_PATH

def evaluate():
    model = mlflow.sklearn.load_model(MODEL_PATH)

    df = load_data(DATA_PATH)
    X, y = split_features_target(df)

    predictions = model.predict(X)

    print("R2:", r2_score(y, predictions))
    print("RMSE:", mean_squared_error(y, predictions, squared=False))

if __name__ == "__main__":
    evaluate()
