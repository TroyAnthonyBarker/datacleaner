import pandas as pd

def na_handler(df: pd.DataFrame, strategy: str = 'mean'):
    """
    Handle missing values in a DataFrame.
    This function provides various strategies to handle missing values in a DataFrame.

    The available strategies are:
    - 'mean': Fill missing values with the mean of the column.
    - 'median': Fill missing values with the median of the column.
    - 'mode': Fill missing values with the mode of the column.
    - 'previous': Fill missing values with the previous value in the column.
    - 'next': Fill missing values with the next value in the column.
    - 'interpolate': Fill missing values using linear interpolation.
    - 'drop': Drop rows with any missing values.

    The strategies 'mean', 'median', 'interpolate' require numeric data types.
    If the DataFrame contains non-numeric data types, these strategies will return the non-numeric data types as provided.

    The strategies 'mode', 'previous' and 'next' can be used with any data type.

    If an invalid strategy is provided, a ValueError will be raised.
    If the input is not a pandas DataFrame, a ValueError will be raised.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    strategy (str): The strategy to use for handling missing values. Options are 'mean', 'median', 'mode', 'previous', 'next', 'interpolate', 'drop'.

    Returns:
    pd.DataFrame: The DataFrame with missing values handled.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
 
    if strategy == 'mean':
        for col in df:
            try:
                df[col] = fill_mean(df[col])
            except ValueError:
                # If the column is non-numeric, skip filling
                continue
        return df
    elif strategy == 'median':
        for col in df:
            try:
                df[col] = fill_median(df[col])
            except ValueError:
                # If the column is non-numeric, skip filling
                continue
        return df
    elif strategy == 'mode':
        return df.apply(fill_mode, axis=0)
    elif strategy == 'previous':
        return df.apply(fill_previous, axis=0)
    elif strategy == 'next':
        return df.apply(fill_next, axis=0)
    elif strategy == 'interpolate':
        for col in df:
            try:
                df[col] = fill_interpolate(df[col])
            except ValueError:
                # If the column is non-numeric, skip filling
                continue
        return df
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', 'next', 'previous', 'interpolate', or 'drop'.")
        

def fill_mean(column: pd.Series) -> pd.Series:
    """
    Fill missing values in a Series with the mean of the Series.
    This function will raise an error if the Series is of non-numeric type.

    Parameters:
    column (pd.Series): The Series to process.

    Returns:
    pd.Series: The Series with missing values filled with the mean.
    """
    if not isinstance(column, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    
    if column.dtype == 'object':
        raise ValueError("Cannot compute mean for non-numeric data types.")
    
    return column.fillna(column.mean())

def fill_median(column: pd.Series) -> pd.Series:
    """
    Fill missing values in a Series with the median of the Series.
    This function will raise an error if the Series is of non-numeric type.

    Parameters:
    column (pd.Series): The Series to process.

    Returns:
    pd.Series: The Series with missing values filled with the median.
    """
    if not isinstance(column, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    
    if column.dtype == 'object':
        raise ValueError("Cannot compute median for non-numeric data types.")
    
    return column.fillna(column.median())

def fill_mode(column: pd.Series) -> pd.Series:
    """
    Fill missing values in a Series with the mode of the Series.

    Parameters:
    column (pd.Series): The Series to process.

    Returns:
    pd.Series: The Series with missing values filled with the mode.
    """
    if not isinstance(column, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    
    return column.fillna(column.mode().iloc[0]) if not column.mode().empty else column

def fill_previous(column: pd.Series) -> pd.Series:
    """
    Fill missing values in a Series with the previous value.
    If the first value is missing, it will be filled with the last value of the Series.

    Parameters:
    column (pd.Series): The Series to process.

    Returns:
    pd.Series: The Series with missing values filled with the previous value.
    """
    if not isinstance(column, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    
    column = column.ffill()

    if pd.isna(column[0]):
        column[0] = column[len(column) - 1]
        
    return column

def fill_next(column: pd.Series) -> pd.Series:
    """
    Fill missing values in a Series with the next value.
    If the last value is missing, it will be filled with the first value of the Series.

    Parameters:
    column (pd.Series): The Series to process.

    Returns:
    pd.Series: The Series with missing values filled with the next value.
    """
    if not isinstance(column, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    
    column = column.bfill()

    if pd.isna(column[len(column) - 1]):
        column[len(column) - 1] = column[0]
        
    return column

def fill_interpolate(column: pd.Series) -> pd.Series:
    """
    Fill missing values in a Series using linear interpolation in both directions.
    This function will raise an error if the Series is of non-numeric type.

    Parameters:
    column (pd.Series): The Series to process.

    Returns:
    pd.Series: The Series with missing values filled using interpolation.
    """
    if not isinstance(column, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    
    if column.dtype == 'object':
        raise ValueError("Cannot interpolate non-numeric data types.")
    
    column = column.interpolate(method='linear', limit_direction='both')

    return column