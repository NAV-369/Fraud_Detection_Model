# Fraud Detection Project README

## Business Objective: Business Need

You are a data scientist at **Adey Innovations Inc.**, a top company in the financial technology sector. Your company focuses on solutions for **e-commerce** and **banking**. Your task is to improve the detection of **fraud cases** for **e-commerce transactions** and **bank credit transactions**. This project aims to create **accurate** and **strong fraud detection models** that handle the unique challenges of both types of transaction data. It also includes using **geolocation analysis** and **transaction pattern recognition** to improve detection.

Good fraud detection greatly improves **transaction security**. By using **advanced machine learning models** and **detailed data analysis**, Adey Innovations Inc. can spot fraudulent activities more accurately. This helps prevent **financial losses** and builds **trust** with customers and financial institutions. A well-designed fraud detection system also makes **real-time monitoring** and **reporting** more efficient, allowing businesses to act quickly and reduce risks.

### Project Goals
This project will involve:

- **Analyzing** and **preprocessing** transaction data.
- **Creating** and **engineering features** that help identify fraud patterns.
- **Building** and **training** machine learning models to detect fraud.
- **Evaluating** model performance and making necessary improvements.
- **Deploying** the models for real-time fraud detection and setting up monitoring for continuous improvement.

---

## Project Tasks

### Task 1: Data Collection and Initial Analysis

#### **Objective**
Gather and explore the transaction dataset to understand its structure and contents.

#### **Steps**
1. **Data Source**: Obtain the dataset `fraud_data.csv`, located in the `data/` folder, containing e-commerce transaction records.
2. **Initial Exploration**:
   - Load the dataset using pandas: `df = pd.read_csv('data/fraud_data.csv')`.
   - Inspect columns: `user_id`, `signup_time`, `purchase_time`, `purchase_value`, `device_id`, `source`, `browser`, `sex`, `age`, `ip_address`, `class`.
   - Check for missing values and data types.
3. **Summary**:
   - `class` column indicates **fraud (1)** or **non-fraud (0)**.
   - `purchase_time` and `signup_time` are timestamps for pattern analysis.
   - `ip_address` can be used for geolocation.

#### **Output**
- A preliminary report on dataset characteristics (e.g., number of transactions, fraud rate).

---

### Task 2: Data Preprocessing and Feature Engineering

#### **Objective**
Clean the data and create features to enhance fraud detection.

#### **Steps**
1. **Preprocessing**:
   - Convert `purchase_time` and `signup_time` to datetime: `pd.to_datetime(df['purchase_time'])`.
   - Handle missing values (if any) by imputation or removal.
   - Encode categorical variables (`source`, `browser`, `sex`) using one-hot encoding.
2. **Feature Engineering**:
   - **Time-Based Features**: Calculate time difference between signup and purchase.
   - **Geolocation**: Convert `ip_address` to country/region using an IP-to-location mapping tool or API.
   - **Transaction Patterns**: Count transactions per `device_id` to detect repeated usage (potential fraud indicator).
   - **Aggregates**: Compute average `purchase_value` per user or device.

#### **Output**
- A preprocessed dataset with new features saved as `processed_fraud_data.csv`.

---

### Task 3: Model Development

#### **Objective**
Build and train machine learning models to detect fraud.

#### **Steps**
1. **Model Selection**:
   - Choose algorithms like **Random Forest**, **XGBoost**, or **Logistic Regression** for their ability to handle imbalanced data.
2. **Train-Test Split**:
   - Split data into 80% training and 20% testing sets.
3. **Training**:
   - Train models on the engineered features, focusing on the `class` target variable.
   - Use techniques like **SMOTE** or class weighting to handle the imbalance between fraud and non-fraud cases.
4. **Feature Importance**:
   - Analyze which features (e.g., time difference, geolocation) contribute most to fraud detection.

#### **Output**
- Trained model files (e.g., `fraud_model.pkl`) saved in a `models/` folder.

---

### Task 4: Model Evaluation and Improvement

#### **Objective**
Assess model performance and refine for better accuracy.

#### **Steps**
1. **Evaluation Metrics**:
   - Use **precision**, **recall**, **F1-score**, and **ROC-AUC** to evaluate, prioritizing recall to catch more fraud cases.
2. **Cross-Validation**:
   - Perform k-fold cross-validation to ensure robustness.
3. **Hyperparameter Tuning**:
   - Optimize model parameters using grid search or random search.
4. **Improvement**:
   - Adjust features or model based on evaluation results (e.g., add more geolocation granularity).

#### **Output**
- A performance report with metrics and a finalized model.

---

### Task 5: Model Deployment and Dashboard Creation

#### **Objective**
Deploy the fraud detection model and create a dashboard for real-time monitoring.

#### **Steps**
1. **API Development (`app.py`)**:
   - Build a Flask API to serve fraud data from `data/fraud_data.csv`.
   - Endpoints:
     - `/api/summary`: Total transactions, fraud cases, and percentage.
     - `/api/fraud_over_time`: Daily fraud counts.
     - `/api/fraud_by_geography`: Fraud by country.
     - `/api/fraud_by_device_browser`: Fraud by browser (since `device_type` isn’t available).
   - Run on **port 5002**.

2. **Model Serving (`server_model.py`)**:
   - Create a Flask API to serve model predictions.
   - Endpoint: `/api/predict` for real-time fraud classification.
   - Run on **port 5001**.

3. **Dashboard (`dashboard.py`)**:
   - Use Dash to visualize fraud data from `app.py`.
   - Graphs:
     - **Graph 1**: Line chart of fraud trend over time.
     - **Graph 2**: Bar chart of fraud by browser.
     - **Graph 3**: Bar chart of fraud by region (country).
     - **Graph 4**: Bar chart of daily fraud counts.
   - Run on **port 5003**.

#### **Files**
- **`app.py`**: API server for data endpoints.
- **`server_model.py`**: Model prediction server (optional if model deployment is required).
- **`dashboard.py`**: Dashboard for visualization.

#### **Directory Structure**
```
project_folder/
├── data/
│   └── fraud_data.csv
├── models/
│   └── fraud_model.pkl (optional)
├── app.py
├── dashboard.py
└── server_model.py
```

#### **Running the Project**
1. Start the API:
   ```bash
   python app.py
   ```
   - Runs on `http://localhost:5002`.
2. Start the dashboard:
   ```bash
   python dashboard.py
   ```
   - Runs on `http://localhost:5003`.
3. (Optional) Start the model server:
   ```bash
   python server_model.py
   ```
   - Runs on `http://localhost:5001`.

#### **Output**
- A live dashboard at `http://localhost:5003` displaying fraud insights.
- (Optional) A prediction API at `http://localhost:5001/api/predict`.

---

## Conclusion

This project fulfills Adey Innovations Inc.’s need for a robust fraud detection system by leveraging data analysis, machine learning, and real-time monitoring. The combination of preprocessed transaction data, trained models, and an interactive dashboard ensures **accurate fraud detection**, **enhanced security**, and **customer trust**, aligning with the company’s goals in the financial technology sector.
