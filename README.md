# Task 2 - Model Building and Training

This notebook covers the implementation of **Task 2** for the fraud detection project. The task involves building, training, and evaluating multiple machine learning and deep learning models for fraud detection on two datasets: `creditcard` and `Fraud_Data`.

---

## Table of Contents
1. [Data Preparation](#data-preparation)
2. [Model Selection](#model-selection)
3. [Model Training and Evaluation](#model-training-and-evaluation)
4. [Performance Summary](#performance-summary)
5. [MLOps: Experiment Tracking with MLflow](#mlops-experiment-tracking-with-mlflow)
6. [Next Steps](#next-steps)

---

## Data Preparation

### 1. Feature and Target Separation
- Separated features (`X`) and target (`y`) for both datasets:
  - `creditcard`: Target column = `Class`
  - `Fraud_Data`: Target column = `class`

### 2. Train-Test Split
- Split the data into training and testing sets (80% train, 20% test) using `train_test_split` from `sklearn`.

---

## Model Selection

The following models were selected for comparison:
1. **Machine Learning Models**:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Gradient Boosting
   - Multi-Layer Perceptron (MLP)

2. **Deep Learning Models**:
   - Convolutional Neural Network (CNN)
   - Recurrent Neural Network (RNN)
   - Long Short-Term Memory (LSTM)

---

## Model Training and Evaluation

### 1. Machine Learning Models
- Trained and evaluated using `sklearn`:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - MLP

### 2. Deep Learning Models
- Trained and evaluated using `TensorFlow/Keras`:
  - CNN
  - RNN
  - LSTM

### 3. Evaluation Metrics
- Metrics computed for each model:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - ROC-AUC

---

## Performance Summary

### 1. Performance Summary Table
- A table summarizing the performance metrics for all models on both datasets:
  - `creditcard`
  - `Fraud_Data`

### 2. Visualizations
- Plots comparing model performance (e.g., ROC-AUC scores).

---

## MLOps: Experiment Tracking with MLflow

### 1. Logging Experiments
- Used `MLflow` to log:
  - Parameters (e.g., dataset, model)
  - Metrics (e.g., accuracy, precision, recall, F1-score, ROC-AUC)
  - Models (e.g., trained model artifacts)

### 2. Viewing Logs
- Started the MLflow UI using:
  ```bash
  mlflow ui