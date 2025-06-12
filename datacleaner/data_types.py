import pandas as pd

def convert_to_numeric(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Convert a specified column in a DataFrame to numeric format.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to convert.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified column converted to numeric.
    """

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    try:
        df[column_name] = pd.to_numeric(df[column_name], errors='raise')
        return df
    except ValueError:
        raise ValueError(f"Could not convert column '{column_name}' to numeric, please check the data.")

def convert_to_classification(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Convert a specified column in a DataFrame to categorical format.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to convert.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified column converted to categorical.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    try:
        df[column_name] = df[column_name].astype('category')
        return df
    except ValueError:
        raise ValueError(f"Could not convert column '{column_name}' to categorical, please check the data")

def convert_to_float(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Convert a specified column in a DataFrame to float format.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to convert.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified column converted to float.
    """

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    try:
        df[column_name] = df[column_name].astype(float)
        return df
    except ValueError:
        raise ValueError(f"Could not convert column '{column_name}' to float, please check the data.")