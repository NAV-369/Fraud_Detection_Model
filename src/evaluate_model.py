import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def load_model(model_path):
    """Load the trained model from a file."""
    return joblib.load(model_path)

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

if __name__ == "__main__":
    df = load_data("fraud_data.csv")
    X = df.drop(columns=["Class"])
    y = df["Class"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = load_model("model.pkl")
    accuracy, report = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
