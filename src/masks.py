

def card_number_encoder(number_card: str) -> str:
    """Функция принимает номер карты и зашифровывает его"""
    if len(number_card) == 16:
        return f"{number_card[0:4]} {number_card[5:7]}** **** {number_card[12:17]}"
    if len(number_card) != 16:
        return "Номер карты введен неверно"


def account_number_encoder(number_encoder: str) -> str:
    """Функция принимает счет карты и зашифровывает его"""
    if len(number_encoder) == 20:
        return f"**{number_encoder[16:21]}"
    if len(number_encoder) != 20:
        return "Номер счета введен неверно"
