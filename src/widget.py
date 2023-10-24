from typing import Callable
from masks import card_number_encoder
from masks import account_number_encoder

card = card_number_encoder('8990922113665229')
check = account_number_encoder('64686473678894779589')
def mask_with_card_type(type_card_or_account: str, func: Callable) -> str:
    if func == card_number_encoder:
        return f'{type_card_or_account} {func}'
    else:
        return f'{type_card_or_account} {func}'


def convert_to_date(string: str) -> str:
    return f'{string[8:10]}.{string[5:7]}.{string[0:4]}'

print(mask_with_card_type("Счет", check))