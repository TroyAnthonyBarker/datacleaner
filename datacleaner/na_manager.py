import pandas as pd

def na_handler(df: pd.DataFrame, strategy: str = 'mean'):
    """
    Handle missing values in a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    strategy (str): The strategy to use for handling missing values.
                    Options are 'mean', 'median', 'mode', 'drop'.

    Returns:
    pd.DataFrame: The DataFrame with missing values handled.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
       
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'previous':
        return df.ffill()
    elif strategy == 'next':
        return df.bfill()
    elif strategy == 'interpolate':
        return df.interpolate()
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', 'next', 'previous', 'interpolate', or 'drop'.")