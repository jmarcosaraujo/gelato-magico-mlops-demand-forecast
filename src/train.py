import os
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error
from src.preprocess import load_data, split_features_target
from src.config import DATA_PATH, MODEL_PATH, MODEL_DIR, MLFLOW_EXPERIMENT

def train():
    mlflow.set_experiment(MLFLOW_EXPERIMENT)

    df = load_data(DATA_PATH)
    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    with mlflow.start_run():

        model = GradientBoostingRegressor()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        r2 = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions, squared=False)

        mlflow.log_metric("r2_score", r2)
        mlflow.log_metric("rmse", rmse)

        mlflow.sklearn.log_model(model, "model")

        os.makedirs(MODEL_DIR, exist_ok=True)
        mlflow.sklearn.save_model(model, MODEL_PATH)

        print(f"Modelo salvo em {MODEL_PATH}")
        print(f"R2: {r2}")
        print(f"RMSE: {rmse}")

if __name__ == "__main__":
    train()
