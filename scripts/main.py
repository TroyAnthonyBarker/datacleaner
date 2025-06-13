import pandas as pd
from datacleaner import convert_to_numeric
from datacleaner import na_handler

df = pd.DataFrame({
    'A': ['1', '2', None, 'four', '5'],
    'B': ['a', None, 'c', 'd', 'e'],
    'C': [None, None, None, None, 10],
    'D': [1.0, 2.5, None, 4.5, 5.0],
})

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Convert columns to numeric where applicable
df['A'] = convert_to_numeric(df['A'])

print("\nDataFrame after converting column 'A' to numeric:")
print(df)

# Use the NA manager to handle missing values
df_mean = na_handler(df.copy(), strategy='mean')
df_median = na_handler(df.copy(), strategy='median')
df_mode = na_handler(df.copy(), strategy='mode')
df_prev = na_handler(df.copy(), strategy='previous')
df_next = na_handler(df.copy(), strategy='next')
df_interpolate = na_handler(df.copy(), strategy='interpolate')
df_drop = na_handler(df.copy(), strategy='drop')

print("\nDataFrame after filling NA values with mean:")
print(df_mean)

print("\nDataFrame after filling NA values with median:")
print(df_median)

print("\nDataFrame after filling NA values with mode:")
print(df_mode)

print("\nDataFrame after filling NA values with previous value:")
print(df_prev)

print("\nDataFrame after filling NA values with next value:")
print(df_next)

print("\nDataFrame after filling NA values with interpolation:")
print(df_interpolate)

print("\nDataFrame after dropping rows with any NA values:")
print(df_drop)