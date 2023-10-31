from src.masks import card_number_encoder
from src.masks import account_number_encoder
import pytest
#from src.all_additional_tasks import directory_dictionary
#from src.all_additional_tasks import first_and_last_letter
#from src.all_additional_tasks import maximum_product
#from src.all_additional_tasks import product_sorting
#from src.processing import list_dictionaries_with_key
#from src.processing import sorted_list_of_dict
#from src.widget import mask_with_card_type
#from src.widget import convert_to_date


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
