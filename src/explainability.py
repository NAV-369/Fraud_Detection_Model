import shap
import pandas as pd
import joblib

def load_model(model_path):
    """Load the trained model from a file."""
    return joblib.load(model_path)

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def explain_model(model, X_sample):
    """Generate SHAP values for model explainability."""
    explainer = shap.Explainer(model, X_sample)
    shap_values = explainer(X_sample)
    shap.summary_plot(shap_values, X_sample)

if __name__ == "__main__":
    df = load_data("fraud_data.csv")
    X = df.drop(columns=["Class"])
    model = load_model("model.pkl")
    explain_model(model, X.sample(100, random_state=42))
