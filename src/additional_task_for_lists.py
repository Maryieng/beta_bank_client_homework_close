from operator import mul
from typing import Any


def first_and_last_letter(list_strings: list[str]) -> list[str]:
    """Функция принимает список слов и возвращает список слов у которых первая и последняя буква одинаковые"""
    new_list = []
    for word in list_strings:
        if word == '':
            new_list.append(word)
        elif word[0] == word[-1]:
            new_list.append(word)
    return new_list


def maximum_product(list_numbers: list[int]) -> Any:
    """Функция принимает список цифр и возвращает максимальное произведение двух значений из списка"""
    sort_list_numbers = sorted(list_numbers)
    return max(mul(*sort_list_numbers[:2]), mul(*sort_list_numbers[-2:]))
