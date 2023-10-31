from typing import Any


def card_number_encoder(number_card: str) -> Any:
    """Функция принимает номер карты и зашифровывает его"""
    if len(number_card) == 16:
        return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:17]}"
    if len(number_card) != 16:
        return "Номер карты введен неверно"


def account_number_encoder(number_encoder: str) -> Any:
    """Функция принимает счет карты и зашифровывает его"""
    if len(number_encoder) == 20:
        return f"**{number_encoder[16:21]}"
    if len(number_encoder) != 20:
        return "Номер счета введен неверно"
