import pytest
import pandas as pd
import numpy as np

from datacleaner.data_types import (
    convert_to_datetime,
    convert_to_numeric,
    encode_labels
)

def test_convert_to_datetime_valid_and_invalid():
    s = pd.Series(['2020-01-01', 'not_a_date', '2021-12-31'])
    result = convert_to_datetime(s)
    assert pd.isna(result[1])
    assert result[0] == pd.Timestamp('2020-01-01')
    assert result[2] == pd.Timestamp('2021-12-31')
    assert result.dtype == 'datetime64[ns]'

def test_convert_to_numeric_valid_and_invalid():
    s = pd.Series(['1', '2.5', 'not_a_number', None])
    result = convert_to_numeric(s)
    assert result[0] == 1
    assert result[1] == 2.5
    assert np.isnan(result[2])
    assert np.isnan(result[3])
    assert result.dtype == 'float64'

def test_encode_labels_basic():
    s = pd.Series(['cat', 'dog', 'cat', 'bird'])
    result = encode_labels(s)
    # The codes are assigned in lexicographical order: bird=0, cat=1, dog=2
    assert list(result) == [1, 2, 1, 0]

def test_encode_labels_with_nan():
    s = pd.Series(['apple', None, 'banana', 'apple'])
    result = encode_labels(s)
    # None/NaN should be encoded as -1
    assert -1 in result.values
    assert set(result.values) == {0, 1, -1}