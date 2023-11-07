from typing import Any


def list_dictionaries_with_key(list_dictionary: list[dict[str, Any]], state="EXECUTED") -> list[dict[str, Any]]:
    """принимает на вход список словарей и значение для ключа state
     и возвращает новый список, у которых ключ state"""
    return [min_dict for min_dict in list_dictionary if min_dict['state'] == state]


def sorted_list_of_dict(list_dictionary: list[dict[str, Any]], sort_desired: bool) -> list[dict[str, Any]]:
    """принимает на вход список словарей и возвращает новый список, где словари отсортированы по убыванию даты.
    Если не указано иначе"""
    if not sort_desired:
        return sorted(list_dictionary, key=lambda x: x['date'], reverse=True)
    return sorted(list_dictionary, key=lambda x: x['date'])
