import os
import re
from typing import Any

import pandas as pd


def reading_data_from_file_csv(file_name: str) -> Any:
    """ Считывание из csv файла данные"""
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', file_name)
    return pd.read_csv(file_path, encoding='utf-8')


def reading_data_from_file_xlsx(file_name: str) -> Any:
    """ Считывание из xlsx файла данные """
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', file_name)
    return pd.read_excel(file_path, na_values=["NA", "N/A", "missing"])


def searching_data_by_string(list_dictionaries: list[dict], string: str) -> list[dict]:
    """ принимает список словарей с данными о банковских операциях и
    строку поиска и возвращать список словарей, у которых в описании есть данная строка. """
    result = []
    pattern = re.compile(string, re.IGNORECASE)
    for dictionary in list_dictionaries:
        description = dictionary.get('description', '')
        if re.search(pattern, description):
            result.append(dictionary)
    return result


def search_dictionaries_by_category(list_dictionaries: list[dict], category_dictionary: dict) -> dict:
    """ принимает список словарей с данными о банковских операциях и категорий операций. возвращать словарь,
     в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    operation_count = {category: 0 for category in category_dictionary.values()}
    for transaction in list_dictionaries:
        category = transaction.get('description')
        if category in operation_count:
            operation_count[category] += 1
    return operation_count
