from flask import Flask, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Construct the path to the CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'data', 'fraud_data.csv')

# Load dataset
try:
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found at: {data_path}")
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully from:", data_path)
    print("Columns in dataset:", df.columns.tolist())
    print("First few rows:\n", df.head())

    # Ensure 'purchase_time' is datetime if present
    if 'purchase_time' in df.columns:
        df['purchase_time'] = pd.to_datetime(df['purchase_time'], errors='coerce')

    # Ensure 'class' column exists
    if 'class' not in df.columns:
        raise KeyError("Column 'class' not found in dataset.")

except Exception as e:
    raise Exception(f"Error loading dataset: {e}")

# Flask API Endpoints
@app.route('/api/summary', methods=['GET'])
def get_summary():
    try:
        total_transactions = len(df)
        fraud_cases = df[df['class'] == 1].shape[0]
        fraud_percentage = round((fraud_cases / total_transactions) * 100, 2)
        return jsonify({
            'total_transactions': total_transactions,
            'fraud_cases': fraud_cases,
            'fraud_percentage': fraud_percentage
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/fraud_over_time', methods=['GET'])
def fraud_over_time():
    try:
        if 'purchase_time' not in df.columns:
            return jsonify({"error": "Column 'purchase_time' not found."}), 400
        fraud_df = df[df['class'] == 1].groupby(df['purchase_time'].dt.date).size().reset_index(name='count')
        fraud_df.rename(columns={'purchase_time': 'date'}, inplace=True)
        return jsonify(fraud_df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/fraud_by_geography', methods=['GET'])
def fraud_by_geography():
    try:
        if 'country' not in df.columns:
            return jsonify({"error": "Column 'country' not found."}), 400
        fraud_by_geo = df[df['class'] == 1].groupby('country').size().reset_index(name='count')
        return jsonify(fraud_by_geo.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/fraud_by_device_type', methods=['GET'])
def fraud_by_device_type():
    try:
        if 'device_type' not in df.columns:
            return jsonify({"error": "Column 'device_type' not found."}), 400
        fraud_by_type = df[df['class'] == 1].groupby('device_type').size().reset_index(name='count')
        return jsonify(fraud_by_type.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Run on port 5002