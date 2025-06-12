import pandas as pd

def _raise_error_convert(column_name: str) -> None:
    """
    Raise a ValueError with a generic message.
    
    This function is used to raise an error when a specific condition is not met.
    """
    raise ValueError(f"Could not convert column '{column_name}', please check the data.")

def _raise_error_column(column_name: str) -> None:
    """
    Raise a ValueError indicating that the specified column does not exist.
    
    This function is used to raise an error when a column is not found in the DataFrame.
    """
    raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

def convert_to_datetime(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Convert a specified column in a DataFrame to datetime format.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to convert.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified column converted to datetime.
    """

    if column_name not in df.columns:
        _raise_error_column(column_name)
    
    try:
        df[column_name] = pd.to_datetime(df[column_name], errors='raise')
        return df
    except (TypeError, ValueError):
        _raise_error_convert(column_name)

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
        _raise_error_column(column_name)
    
    try:
        df[column_name] = pd.to_numeric(df[column_name], errors='raise')
        return df
    except ValueError:
        _raise_error_convert(column_name)
    
def encode_labels(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encode a specified column in a DataFrame using label encoding.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to encode.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified column encoded.
    """
    
    if column_name not in df.columns:
        _raise_error_column(column_name)
    
    try:
        df[column_name] = df[column_name].astype('category').cat.codes
        return df
    except Exception:
        _raise_error_convert(column_name)

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
        _raise_error_column(column_name)
    
    try:
        df[column_name] = df[column_name].astype(float)
        return df
    except ValueError:
        _raise_error_convert(column_name)