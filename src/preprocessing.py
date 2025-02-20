import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """Load dataset from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None

def handle_missing_values(df, strategy='drop'):
    """Handle missing values by dropping or imputing."""
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'mean':
        return df.fillna(df.mean())
    else:
        print("Invalid strategy. Use 'drop' or 'mean'.")
        return df

def encode_categorical_features(df, categorical_columns):
    """Encode categorical variables using one-hot encoding."""
    return pd.get_dummies(df, columns=categorical_columns)

def split_data(df, target_column, test_size=0.2, random_state=42):
    """Split dataset into training and testing sets."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

if __name__ == "__main__":
    df = load_data("fraud_data.csv")
    if df is not None:
        df = handle_missing_values(df, strategy='mean')
        df = encode_categorical_features(df, ["device", "browser"])
        X_train, X_test, y_train, y_test = split_data(df, "Class")
        print("Preprocessing complete.")
