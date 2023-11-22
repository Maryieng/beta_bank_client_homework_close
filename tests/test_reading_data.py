import unittest.mock as mock

import pandas as pd
import pytest

from src.reading_data import reading_data_from_file_csv, reading_data_from_file_xlsx


@mock.patch('src.reading_data.pd.read_csv')
def test_reading_data_from_file_csv(mock_read_csv):
    file_name = 'example.csv'
    expected_data = [['Mary', 27], ['Artem', 37]]
    mock_read_csv.return_value = expected_data
    result = reading_data_from_file_csv(file_name)
    assert result == expected_data
    mock_read_csv.assert_called_once_with(mock.ANY, encoding='utf-8')


@mock.patch('src.reading_data.pd.read_excel')
def test_file_exists(mock_read_excel):
    file_name = "example.xlsx"
    mock_read_excel.return_value = pd.DataFrame()
    result = reading_data_from_file_xlsx(file_name)
    assert isinstance(result, pd.DataFrame)
    mock_read_excel.assert_called_once()


@mock.patch('src.reading_data.pd.read_excel')
def test_invalid_file(mock_read_excel):
    file_name = "invalid_file.xlsx"
    mock_read_excel.side_effect = FileNotFoundError()
    with pytest.raises(FileNotFoundError):
        reading_data_from_file_xlsx(file_name)
    mock_read_excel.assert_called_once()
