from flask import Flask, jsonify, request
import pandas as pd
import os
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Construct the path to the CSV file and model
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'data', 'fraud_data.csv')
model_path = os.path.join(current_dir, 'models', 'fraud_model.pkl')  # Hypothetical model file

# Load dataset
try:
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found at: {data_path}")
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully from:", data_path)
    print("Columns in dataset:", df.columns.tolist())
    print("First few rows:\n", df.head())
    if 'purchase_time' in df.columns:
        df['purchase_time'] = pd.to_datetime(df['purchase_time'], errors='coerce')
    if 'class' not in df.columns:
        raise KeyError("Column 'class' not found in dataset.")
except Exception as e:
    raise Exception(f"Error loading dataset: {e}")

# Load model (placeholder)
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully from:", model_path)
except FileNotFoundError:
    print("Model file not found. Prediction endpoint will return dummy data.")
    model = None

# Prediction endpoint
@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        if not model:
            return jsonify({"error": "Model not loaded. Using dummy response."}), 500
        data = request.get_json()
        features = pd.DataFrame([data])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].tolist()
        return jsonify({
            'prediction': int(prediction),
            'probability': probability
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on port 5001