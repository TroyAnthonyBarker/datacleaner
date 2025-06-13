import pandas as pd

def convert_to_datetime(column: pd.Series) -> pd.Series:
    """
    Convert a pandas Series to datetime format.
    This function attempts to convert the Series to datetime format, coercing errors to NaT.

    Parameters:
    column (pd.Series): The Series to convert.

    Returns:
    pd.Series: The Series converted to datetime format.
    """
    return pd.to_datetime(column, errors='coerce')

def convert_to_numeric(column: pd.Series) -> pd.Series:
    """
    Convert a pandas Series to numeric format.
    This function attempts to convert the Series to numeric format, coercing errors to NaN.

    Parameters:
    column (pd.Series): The Series to convert.

    Returns:
    pd.Series: The Series converted to numeric format.
    """
    return pd.to_numeric(column, errors='coerce')

    
def encode_labels(column: pd.Series) -> pd.Series:
    """
    Encode categorical labels in a pandas Series to numeric codes.
    This function converts the Series to a categorical type and then encodes the categories as numeric codes.

    Parameters:
    column (pd.Series): The Series to encode.

    Returns:
    pd.Series: The Series with categorical labels encoded as numeric codes.
    """

    return column.astype('category').cat.codes