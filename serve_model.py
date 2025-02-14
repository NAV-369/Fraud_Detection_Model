from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Define the model path (relative to the script location)
model_path = os.path.join(os.path.dirname(__file__), "notebooks", "random_forest_fraud.pkl")

# Load the trained model
try:
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}")
    exit(1)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validate input format
        if "features" not in data:
            return jsonify({"error": "Missing 'features' in request JSON"}), 400
        
        features = np.array(data["features"]).reshape(1, -1)

        # Check if input shape matches the model's expectation
        if features.shape[1] != model.n_features_in_:
            return jsonify({"error": f"Expected {model.n_features_in_} features, but got {features.shape[1]}"}), 400

        # Make prediction
        prediction = model.predict(features)
        return jsonify({"fraud_prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)