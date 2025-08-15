from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def test_predict_shape():
    # Create dummy classification data
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    preds = model.predict(X_test)

    # Assert shape matches number of test samples
    assert preds.shape[0] == X_test.shape[0], "Prediction length does not match input samples"
