import pandas as pd

def create_time_features(df, timestamp_column):
    """Extract time-based features from a timestamp column."""
    df[timestamp_column] = pd.to_datetime(df[timestamp_column])
    df['hour_of_day'] = df[timestamp_column].dt.hour
    df['day_of_week'] = df[timestamp_column].dt.dayofweek
    return df

def transaction_frequency(df, user_column):
    """Compute transaction frequency per user."""
    freq = df[user_column].value_counts().rename("transaction_count")
    return df.merge(freq, left_on=user_column, right_index=True)

def normalize_features(df, columns):
    """Normalize specified numerical features."""
    df[columns] = (df[columns] - df[columns].min()) / (df[columns].max() - df[columns].min())
    return df

if __name__ == "__main__":
    df = pd.read_csv("fraud_data.csv")
    df = create_time_features(df, "timestamp")
    df = transaction_frequency(df, "user_id")
    df = normalize_features(df, ["transaction_amount", "transaction_count"])
    print("Feature engineering complete.")
