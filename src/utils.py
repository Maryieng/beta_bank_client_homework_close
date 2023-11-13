import json
import os
from typing import Any

import requests


def getting_data_from_file(filename: str) -> Any:
    """ считывает из файла данные """
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', filename)
    with open(file_path, encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


list_of_operations = getting_data_from_file('operations.json')


def transaction_amount_in_rubles(id_operation: int) -> Any:
    """ принимает на вход транзакцию и возвращает сумму транзакции в рублях, возвращает тип float """
    specific_operation = [operation for operation in list_of_operations
                          if operation.get("id") == id_operation]
    operation_dict = specific_operation[0]
    if operation_dict["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation_dict["operationAmount"]["amount"])
    else:
        print("ValueError: Операция совершена не в рублях")
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        dollar_exchange_rate = data['Valute']['USD']['Value']
        return round(dollar_exchange_rate * float(operation_dict["operationAmount"]["amount"]), 2)
