from typing import Any, Generator


def filter_by_currency(lst_transactions: list[dict[str, Any]], currency: str) -> Generator:
    """ Принимает список словарей и возвращает итератор, который выдает по очереди операции,
     в которых указана заданная валюта. """
    for transaction in lst_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transaction: list[dict[str, int]]) -> Generator:
    """ Принимает список словарей и возвращает описание каждой операции по очереди."""
    for description in transaction:
        yield description["description"]


def card_number_generator(start: int, finish: int) -> Generator:
    """ Генератор номера карт в формате "XXXX XXXX XXXX XXXX".
     (диапазоны передаются как параметры генератора)."""
    number_zeros = 16 - len(str(finish))
    for number in range(start, finish + 1):
        number_generator = (number_zeros * '0') + str(number)
        yield f'{number_generator[0:4]} {number_generator[4:8]} {number_generator[8:12]} {number_generator[12:17]}'
