import pandas as pd

def na_handle(df: pd.DataFrame, strategy: str = 'mean'):
    """
    Handle missing values in a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    strategy (str): The strategy to use for handling missing values.
                    Options are 'mean', 'median', 'mode', 'drop'.

    Returns:
    pd.DataFrame: The DataFrame with missing values handled.
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', or 'drop'.")