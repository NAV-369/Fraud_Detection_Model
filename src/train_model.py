import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def train_model(X_train, y_train):
    """Train a RandomForest model."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, filename="model.pkl"):
    """Save the trained model to a file."""
    joblib.dump(model, filename)

if __name__ == "__main__":
    df = load_data("fraud_data.csv")
    X = df.drop(columns=["Class"])
    y = df["Class"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    save_model(model)
    print("Model training complete.")
