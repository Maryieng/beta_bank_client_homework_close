from typing import Any

import pytest

from src.masks import account_number_encoder, card_number_encoder
from src.processing import list_dictionaries_with_key, sorted_list_of_dict
from src.widget import convert_to_date, mask_with_card_type


@pytest.fixture
def my_number_card() -> str:
    return '7000792289606361'


@pytest.fixture
def my_account_card() -> str:
    return '73654108430135874305'


def test_card_number_encoder(my_number_card: str) -> None:
    assert card_number_encoder(my_number_card) == '7000 79** **** 6361'
    assert card_number_encoder('700079228960636111') == "Номер карты введен неверно"
    assert card_number_encoder('') == "Номер карты введен неверно"


def test_account_number_encoder(my_account_card: str) -> None:
    assert account_number_encoder(my_account_card) == '**4305'
    assert account_number_encoder('73654108430135874305111') == "Номер счета введен неверно"
    assert account_number_encoder('') == "Номер счета введен неверно"


@pytest.mark.parametrize("input_value, expected_result",
                         [('счет 73654108430135874305', 'Счет **4305'),
                          ('Visa Platinum 7000792289606361', "Visa Platinum 7000 79** **** 6361")])
def test_mask_with_card_type(input_value: str, expected_result: str) -> None:
    assert mask_with_card_type(input_value) == expected_result


def test_convert_to_date() -> None:
    assert convert_to_date("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.mark.parametrize('lst, exit_final',
                         [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_list_dictionaries_with_key(lst: list[Any], exit_final: list[Any]) -> None:
    assert list_dictionaries_with_key(lst) == exit_final


@pytest.mark.parametrize("input_value, expected_result",
                         [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_sorted_list_of_dict(input_value: list[Any], expected_result: list[Any]) -> None:
    assert sorted_list_of_dict(input_value, False) == expected_result
    assert sorted_list_of_dict(input_value, True) == expected_result[::-1]
