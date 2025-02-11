# Task 3: Feature Engineering for Credit Risk Project

# Objective
# The objective of Task 3 is to create meaningful features for a credit risk prediction model. 
# This task involves aggregating existing features, extracting new ones, encoding categorical variables, 
# handling missing values, and normalizing/standardizing numerical features. 
# These processed features will be used to train the model for credit risk prediction.

# Steps and Deliverables

## 1. Aggregate Features
# - Combine existing features to create new aggregate features that can improve the model's predictive power.
# Examples:
# - Total credit balance across accounts.
# - Average monthly spending or income.
# - Count of missed payments or credit inquiries.

# Example code to create aggregate features:
# X_train['total_balance'] = X_train[['credit_balance', 'loan_balance']].sum(axis=1)

## 2. Extract New Features
# - Identify new features based on domain knowledge or exploratory analysis.
# Examples:
# - Duration of the relationship with the bank or credit institution.
# - Frequency of recent large transactions.
# - Ratio of credit utilization (credit balance vs. limit).

# Example code to create new features:
# X_train['credit_utilization'] = X_train['credit_balance'] / X_train['credit_limit']

## 3. Encode Categorical Variables
# - Categorical variables should be transformed into numerical representations.
# Possible methods include:
# - One-hot encoding for nominal categories.
# - Label encoding for ordinal categories.

# Example code to encode categorical variables:
# from sklearn.preprocessing import OneHotEncoder
# encoder = OneHotEncoder(sparse=False)
# X_train_encoded = encoder.fit_transform(X_train[['account_type']])

## 4. Handle Missing Values
# - Address missing data by using appropriate techniques:
# - Imputation (mean, median, or mode).
# - Drop missing values if too many records are incomplete.
# - Use domain-specific techniques when applicable.

# Example code to handle missing values:
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(strategy='mean')
# X_train_imputed = imputer.fit_transform(X_train)

## 5. Normalization/Standardization
# - Normalize or standardize numerical features to ensure they are on a similar scale:
# - Normalization: Scale features to a [0, 1] range.
# - Standardization: Scale features to have zero mean and unit variance.

# Example code to standardize features:
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train[['credit_balance', 'loan_balance']])

## 6. Feature Selection (Optional)
# - Use techniques such as mutual information, recursive feature elimination, or feature importance from models 
# (e.g., tree-based models) to select the most important features for the model.

# Example code for feature selection:
# from sklearn.feature_selection import SelectKBest, mutual_info_classif
# selector = SelectKBest(mutual_info_classif, k='all')
# X_train_selected = selector.fit_transform(X_train, y_train)

