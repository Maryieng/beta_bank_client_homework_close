from operator import mul
from typing import Any
import os
import os.path


def directory_dictionary(path="../src", recursive_counting=None) -> None:
    """Функция принимает путь до директории и выводит словарь с содержимым"""
    print(
        f"""files: {len([name for name in os.listdir(path) if os.path.isfile(name)])}
folders: {len([name for name in os.listdir(path) if not os.path.isfile(name)])}"""
    )
    if recursive_counting is not None:
        for root, dirs, files in os.walk(path):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))


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
