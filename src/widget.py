from typing import Callable
from masks import card_number_encoder
from masks import account_number_encoder


def mask_with_card_type(type_card_or_account: str, func: Callable) -> str:
    """Функция принимает номер и тип карты/счета и возвращает в виде:
     "Visa Platinum 7000 79** **** 6361 / Счет **4305" """
    if func == card_number_encoder:
        return f'{type_card_or_account} {func}'
    else:
        return f'{type_card_or_account} {func}'


def convert_to_date(string: str) -> str:
    """Функция принимает строку и возвращает в виде: "11.07.2018" """
    return f'{string[8:10]}.{string[5:7]}.{string[0:4]}'


number_object = input('Укажите объект номера. Карта/счет? \n').lower()
user_number_input = str(input('Введите номер счета/карты \n'))
if number_object == "карта":
    print(mask_with_card_type(str(input('Тип карты: \n')), card_number_encoder(user_number_input)))
else:
    print(mask_with_card_type("Счет", account_number_encoder(user_number_input)))
