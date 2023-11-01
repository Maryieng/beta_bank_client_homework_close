import pytest

from src.masks import account_number_encoder, card_number_encoder
from src.widget import convert_to_date, mask_with_card_type


@pytest.fixture
def my_number_card():
    return '7000792289606361'


@pytest.fixture
def my_account_card():
    return '73654108430135874305'


def test_card_number_encoder(my_number_card):
    assert card_number_encoder(my_number_card) == '7000 79** **** 6361'
    assert card_number_encoder('700079228960636111') == "Номер карты введен неверно"
    assert card_number_encoder('') == "Номер карты введен неверно"


def test_account_number_encoder(my_account_card):
    assert account_number_encoder(my_account_card) == '**4305'
    assert account_number_encoder('73654108430135874305111') == "Номер счета введен неверно"
    assert account_number_encoder('') == "Номер счета введен неверно"


@pytest.mark.parametrize("input_value, expected_result",
                         [('счет 73654108430135874305', 'Счет **4305'),
                          ('Visa Platinum 7000792289606361', "Visa Platinum 7000 79** **** 6361")])
def test_mask_with_card_type(input_value, expected_result):
    assert mask_with_card_type(input_value) == expected_result


def test_convert_to_date():
    assert convert_to_date("2018-07-11T02:26:18.671407") == "11.07.2018"
