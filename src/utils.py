import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger('__utils__')
file_handler_utils = logging.FileHandler('utils_loger.log', 'w', encoding='utf-8')
file_formatter_utils = logging.Formatter('%(asctime)s %(module)s %(levelname)s %(message)s')
file_handler_utils.setFormatter(file_formatter_utils)
logger.addHandler(file_handler_utils)
logger.setLevel(logging.INFO)


def getting_data_from_file(filename: str) -> Any:
    """ принимает на вход путь до файла и возвращает список словарей. Если есть ошибка,
    функция возвращает пустой список """
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', filename)
    try:
        with open(file_path, encoding='utf-8') as file:
            logger.info(f'файл {filename} загружен')
            return json.load(file)
    except json.JSONDecodeError:
        logger.error(f'файл {filename} не загружен')
        return []
    except FileNotFoundError:
        logger.error(f'файл {filename} не найден')
        return []


def transaction_amount_in_rubles(operation: dict[str, Any]) -> Any:
    """ принимает на вход транзакцию и возвращает сумму транзакции в рублях, возвращает тип float """
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        logger.info(f'транзакция в рублях возвращает {operation["operationAmount"]["amount"]} рублей')
        return float(operation["operationAmount"]["amount"])
    else:
        api_key = os.getenv('api_key')
        url = f"http://api.currencylayer.com/live?access_key={api_key}&currencies=RUB&source=USD"
        response = requests.get(url)
        data = response.json()
        conversion_rate = data['quotes']['USDRUB']
        rub_amount = float(operation["operationAmount"]["amount"]) * conversion_rate
        logger.info(f'транзакция в долларах возвращает {round(rub_amount, 2)} рублей')
        return round(rub_amount, 2)
