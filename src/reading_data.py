import os
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
