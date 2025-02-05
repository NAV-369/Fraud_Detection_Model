# Task 1 - Data Analysis and Preprocessing

## Objective
The objective of Task 1 is to perform comprehensive data analysis and preprocessing on the given datasets. This includes handling missing values, cleaning the data, performing exploratory data analysis (EDA), merging datasets for geolocation analysis, and generating meaningful features for model building.

## Deliverables

### 1. Handle Missing Values
- **Impute or Drop Missing Values**: Identify and address missing values in the dataset by either imputing or removing the rows/columns with missing data based on the context and requirements.

### 2. Data Cleaning
- **Remove Duplicates**: Ensure that the dataset does not contain any duplicate entries to maintain data integrity.
- **Correct Data Types**: Check for columns with incorrect data types and correct them (e.g., converting string representations of numbers to numerical data types).

### 3. Exploratory Data Analysis (EDA)
- **Univariate Analysis**: Perform a detailed analysis of individual features to understand their distribution and detect any anomalies.
- **Bivariate Analysis**: Explore relationships between pairs of features to uncover potential correlations and insights.

### 4. Merge Datasets for Geolocation Analysis
- **Convert IP Addresses to Integer Format**: Convert IP addresses in the dataset to integer format to facilitate efficient processing.
- **Merge Datasets**: Combine the `Fraud_Data.csv` with `IpAddress_to_Country.csv` to enrich the data with geolocation information based on IP addresses.

### 5. Feature Engineering
- **Transaction Frequency and Velocity**: Create new features based on transaction frequency and velocity for `Fraud_Data.csv` to enhance predictive power.
- **Time-Based Features**:
  - `hour_of_day`: Extract the hour of the day from transaction timestamps.
  - `day_of_week`: Extract the day of the week from transaction timestamps.

### 6. Normalization and Scaling
- Normalize and scale the numerical features in the dataset to ensure that models do not become biased toward any feature with a larger scale.

### 7. Encode Categorical Features
- Convert categorical features into numerical representations using appropriate encoding techniques (e.g., One-Hot Encoding or Label Encoding) to make them suitable for model training.

## Steps Taken in the Notebook:
1. **Data Loading**: Import the necessary libraries and load the datasets.
2. **Data Preprocessing**: Handle missing values, clean data, and convert IP addresses.
3. **Exploratory Data Analysis (EDA)**: Conduct univariate and bivariate analysis to understand the data.
4. **Feature Engineering**: Generate transaction-related features, time-based features, and merge geolocation data.
5. **Normalization and Scaling**: Apply scaling techniques to standardize numerical features.
6. **Encode Categorical Features**: Perform encoding on categorical columns for model readiness.

## Tools Used
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For data preprocessing (scaling, encoding).
- **IP2Location or other libraries**: For IP-to-geolocation conversion.

## Expected Outcomes
- A clean and preprocessed dataset ready for model training.
- Feature-rich dataset with additional engineered features such as time-based attributes and geolocation information.