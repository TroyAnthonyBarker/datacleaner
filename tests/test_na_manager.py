import pytest
import pandas as pd

from datacleaner.na_manager import (
    na_handler,
    fill_mean,
    fill_median,
    fill_mode,
    fill_previous,
    fill_next,
    fill_interpolate,
)

@pytest.fixture
def mixed_df():
    return pd.DataFrame({
        'num1': [1, 2, None, 4],
        'num2': [None, 2, 3, 4],
        'obj1': ['foo', None, 'bar', 'baz'],
        'obj2': [None, 'x', 'y', 'z']
    })

def test_na_handler_mean(mixed_df):
    result = na_handler(mixed_df.copy(), 'mean')
    # Numeric columns filled, object columns untouched
    assert result['num1'].isna().sum() == 0
    assert result['num2'].isna().sum() == 0
    assert result['obj1'].isna().sum() == 1
    assert result['obj2'].isna().sum() == 1
    assert result.loc[2, 'num1'] == pytest.approx((1+2+4)/3)
    assert result.loc[0, 'num2'] == pytest.approx((2+3+4)/3)

def test_na_handler_median(mixed_df):
    result = na_handler(mixed_df.copy(), 'median')
    assert result['num1'].isna().sum() == 0
    assert result['num2'].isna().sum() == 0
    assert result['obj1'].isna().sum() == 1
    assert result['obj2'].isna().sum() == 1
    assert result.loc[2, 'num1'] == 2
    assert result.loc[0, 'num2'] == 3

def test_na_handler_mode(mixed_df):
    result = na_handler(mixed_df.copy(), 'mode')
    assert result['num1'].isna().sum() == 0
    assert result['num2'].isna().sum() == 0
    assert result['obj1'].isna().sum() == 0
    assert result['obj2'].isna().sum() == 0

def test_na_handler_previous_next(mixed_df):
    prev = na_handler(mixed_df.copy(), 'previous')
    next_ = na_handler(mixed_df.copy(), 'next')
    # num1
    assert prev['num1'].iloc[2] == 2
    assert next_['num1'].iloc[2] == 4
    # num2
    assert prev['num2'].iloc[0] == 4
    assert next_['num2'].iloc[0] == 2
    # obj1
    assert prev['obj1'].iloc[1] == 'foo'
    assert next_['obj1'].iloc[1] == 'bar'
    # obj2
    assert prev['obj2'].iloc[0] == 'z'
    assert next_['obj2'].iloc[0] == 'x'

def test_na_handler_interpolate(mixed_df):
    result = na_handler(mixed_df.copy(), 'interpolate')
    assert result['num1'].isna().sum() == 0
    assert result['num1'].iloc[2] == 3
    assert result['num2'].isna().sum() == 0
    assert result['num2'].iloc[0] == 4
    # Object columns should remain unchanged
    assert result['obj1'].isna().sum() == 1
    assert result['obj2'].isna().sum() == 1

def test_na_handler_drop(mixed_df):
    result = na_handler(mixed_df.copy(), 'drop')
    # Only rows with no NA in any column remain
    assert len(result) == 1
    assert result.isna().sum().sum() == 0

def test_na_handler_invalid_strategy(mixed_df):
    with pytest.raises(ValueError):
        na_handler(mixed_df, 'invalid')

def test_na_handler_non_dataframe():
    with pytest.raises(ValueError):
        na_handler([1, 2, None], 'mean')

def test_fill_mean_and_median_numeric(mixed_df):
    s1 = mixed_df['num1']
    s2 = mixed_df['num2']
    assert fill_mean(s1).isna().sum() == 0
    assert fill_mean(s2).isna().sum() == 0
    assert fill_median(s1).isna().sum() == 0
    assert fill_median(s2).isna().sum() == 0

def test_fill_mean_and_median_non_numeric(mixed_df):
    s1 = mixed_df['obj1']
    s2 = mixed_df['obj2']
    with pytest.raises(ValueError):
        fill_mean(s1)
    with pytest.raises(ValueError):
        fill_mean(s2)
    with pytest.raises(ValueError):
        fill_median(s1)
    with pytest.raises(ValueError):
        fill_median(s2)

def test_fill_mode(mixed_df):
    s1 = mixed_df['obj1']
    s2 = mixed_df['obj2']
    filled1 = fill_mode(s1)
    filled2 = fill_mode(s2)
    assert filled1.isna().sum() == 0
    assert filled2.isna().sum() == 0

def test_fill_previous_and_next(mixed_df):
    for col in mixed_df.columns:
        s = mixed_df[col]
        prev = fill_previous(s.copy())
        next_ = fill_next(s.copy())
        assert prev.isna().sum() == 0
        assert next_.isna().sum() == 0

def test_fill_interpolate_numeric(mixed_df):
    s1 = mixed_df['num1']
    s2 = mixed_df['num2']
    filled1 = fill_interpolate(s1)
    filled2 = fill_interpolate(s2)
    assert filled1.isna().sum() == 0
    assert filled2.isna().sum() == 0
    assert filled1.iloc[2] == 3
    assert filled2.iloc[0] == 4

def test_fill_interpolate_non_numeric(mixed_df):
    s1 = mixed_df['obj1']
    s2 = mixed_df['obj2']
    with pytest.raises(ValueError):
        fill_interpolate(s1)
    with pytest.raises(ValueError):
        fill_interpolate(s2)