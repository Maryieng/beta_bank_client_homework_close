import json
import os

import pytest

from src.utils import getting_data_from_file, transaction_amount_in_rubles


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


def test_getting_data_from_file_None():
    test_file_name = "test_data.json"
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', test_file_name)
    open(file_path, 'w').close()
    result = getting_data_from_file(test_file_name)
    os.remove(file_path)
    assert result == []


test_getting_data_from_file()


@pytest.mark.parametrize("input_value, expected_result",
                         [(596171168, 79931.03),
                          (895315941, 5240026.38)])
def test_transaction_amount_in_rubles(input_value, expected_result):
    assert transaction_amount_in_rubles(input_value) == expected_result


def test_transaction_amount_in_rubles_console(capsys):
    transaction_amount_in_rubles(895315941)
    captured = capsys.readouterr()
    assert captured.out == "ValueError: Операция совершена не в рублях\n"
