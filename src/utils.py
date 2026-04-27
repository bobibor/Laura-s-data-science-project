import pandas as pd
import numpy as np


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from a given file path.
    """
    return pd.read_csv(file_path)


def basic_info(df: pd.DataFrame) -> dict:
    """
    Return basic information about the dataset.
    """
    info = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum()
    }
    return info


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning: remove duplicates and handle missing values.
    """
    df = df.copy()
    df = df.drop_duplicates()
    df = df.fillna(df.median(numeric_only=True))
    return df


def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Normalize selected columns using Min-Max scaling.
    """
    df = df.copy()
    for col in columns:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical variables using one-hot encoding.
    """
    return pd.get_dummies(df, drop_first=True)


def split_features_target(df: pd.DataFrame, target_column: str):
    """
    Split dataset into features (X) and target (y).
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def train_test_split_manual(X, y, test_size=0.2, random_state=42):
    """
    Simple train/test split without sklearn.
    """
    np.random.seed(random_state)
    indices = np.random.permutation(len(X))
    test_size = int(len(X) * test_size)

    test_idx = indices[:test_size]
    train_idx = indices[test_size:]

    return X.iloc[train_idx], X.iloc[test_idx], y.iloc[train_idx], y.iloc[test_idx]


def evaluate_model(y_true, y_pred) -> dict:
    """
    Basic evaluation metrics.
    """
    accuracy = (y_true == y_pred).mean()

    return {
        "accuracy": round(accuracy, 4)
    }

Изпратено от Outlook за Android
