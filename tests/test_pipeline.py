from src.predict import predict

def test_prediction_positive():
    result = predict(30)
    assert result > 0
