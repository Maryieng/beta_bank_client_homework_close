import json
import os
from unittest import mock
from unittest.mock import patch

from dotenv import load_dotenv

from src.utils import getting_data_from_file, transaction_amount_in_rubles

load_dotenv()


def test_getting_data_from_file():
    test_file_name = "test_data.json"
    expected_data = [
        {"name": "Mary", "age": 27},
        {"name": "Artem", "age": 37},
    ]
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', test_file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(expected_data, file)
    result = getting_data_from_file(test_file_name)
    os.remove(file_path)
    assert result == expected_data


def test_getting_data_from_file_error():
    test_file_name = "test_data.json"
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', test_file_name)
    open(file_path, 'w').close()
    result = getting_data_from_file(test_file_name)
    os.remove(file_path)
    assert result == []


def test_getting_data_from_file_not_found():
    assert getting_data_from_file("test_data.json") == []


@mock.patch("os.getenv")
def test_transaction_in_rubles(mock_getenv):
    operation = {
        "operationAmount": {
            "currency": {
                "code": "RUB"
            },
            "amount": 100.0
        }
    }
    result = transaction_amount_in_rubles(operation)
    assert result == 100.0
    mock_getenv.assert_not_called()


@patch('src.utils.requests.get')
def test_transaction_amount_in_rubles_with_rub_currency(mock_get):
    operation = {
        "operationAmount": {
            "currency": {
                "code": "RUB"
            },
            "amount": 100.0
        }
    }
    result = transaction_amount_in_rubles(operation)
    assert result == 100.0


@patch('src.utils.requests.get')
def test_transaction_amount_in_rubles_with_non_rub_currency(mock_get):
    operation = {
        "operationAmount": {
            "currency": {
                "code": "USD"
            },
            "amount": 100.0
        }
    }
    mock_get.return_value = mock.Mock()
    mock_get.return_value.json.return_value = {
        "quotes": {
            "USDRUB": 75.0
        }
    }
    result = transaction_amount_in_rubles(operation)
    assert result == 7500.0
