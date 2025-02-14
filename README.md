Here’s the README in pure Markdown format with # for headers and other markdown syntax:

# Task 4: Model Serving and API Deployment

## Overview

In this task, we focus on deploying a machine learning model for fraud detection via a REST API. The model is trained using the `RandomForestClassifier` and is served using Flask within a Docker container. This allows real-time prediction by providing input features via a POST request.

## Steps Involved

### 1. **Model Training**

Before deploying the model, ensure that you have a trained model saved in a `.pkl` file. The model used in this task is `random_forest_fraud.pkl`, and it should be trained using your dataset and saved in the appropriate location.

### 2. **Flask API Setup**

Flask will be used to create a simple web API. The API will accept POST requests at the `/predict` endpoint and respond with fraud prediction results. The model is loaded from the saved `.pkl` file when the API is started.

#### Flask API Code:

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load("random_forest_fraud.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get the input data
        features = np.array(data["features"]).reshape(1, -1)  # Prepare features for prediction
        prediction = model.predict(features)  # Get prediction
        return jsonify({"fraud_prediction": int(prediction[0])})  # Return the result as JSON
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

3. Docker Setup

The Flask app is packaged within a Docker container for easy deployment. Below is the Dockerfile that sets up the environment and starts the API server.

Dockerfile:

# Use Python as the base image
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy all files from the current directory to the /app directory in the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5001 for the Flask API
EXPOSE 5001

# Run the Flask API when the container starts
CMD ["python", "serve_model.py"]

4. Building and Running Docker Container

After creating the Dockerfile, build the Docker image using the following command:

docker build -t fraud-detection-model .

Once the build is successful, run the container using:

docker run -p 5001:5001 fraud-detection-model

This starts the Flask server inside the Docker container, exposing port 5001 for external access.

5. Testing the API

To test the API, you can send a POST request from another Python script or tool like Postman or cURL.

Example Python Test Script (API_test.py):

import requests

url = "http://127.0.0.1:5001/predict"
data = {"features": [0.1, 1.2, 3.4, 5.6]}  # Adjust based on your model's expected input format
response = requests.post(url, json=data)
print(response.json())

6. Common Issues and Troubleshooting
	•	Port Conflicts: Ensure that port 5001 is not being used by another application. If necessary, change the port in both Dockerfile and API client script.
	•	Model Not Loading Properly: Ensure that the model file random_forest_fraud.pkl is in the correct location and can be loaded without issues.
	•	API Not Responding: Check the Flask app logs in the Docker container to ensure it’s running correctly and processing requests.

7. Conclusion

With the Docker container running, you can send requests to the API for real-time fraud detection predictions. The model is loaded dynamically when the API starts, and you can scale and deploy the container as needed.

Requirements
	•	Python 3.8+
	•	Flask
	•	scikit-learn
	•	joblib
	•	Docker

Requirements File (requirements.txt):

flask
scikit-learn
joblib

Next Steps
	•	Explore how to improve model performance or update it periodically.
	•	Implement logging and monitoring for the API.
	•	Deploy the API to a cloud platform for scalability.

This Markdown will properly render the headings, code blocks, and sections in a readable way in any Jupyter notebook or Markdown renderer.