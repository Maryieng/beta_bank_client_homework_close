import logging
from typing import Any

logger = logging.getLogger('__masks__')
file_handler_masks = logging.FileHandler('masks_loger.log', 'w', encoding='utf-8')
file_formatter_masks = logging.Formatter('%(asctime)s %(module)s %(levelname)s %(message)s')
file_handler_masks.setFormatter(file_formatter_masks)
logger.addHandler(file_handler_masks)
logger.setLevel(logging.INFO)


def card_number_encoder(number_card: str) -> Any:
    """ Функция принимает номер карты и зашифровывает его """
    if len(number_card) == 16:
        logger.info('Номер карты введен верно')
        return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:17]}"
    if len(number_card) != 16:
        logger.error('Номер карты введен не верно')
        return "Номер карты введен неверно"


def account_number_encoder(number_encoder: str) -> Any:
    """ Функция принимает счет карты и зашифровывает его """
    if len(number_encoder) == 20:
        logger.info('Номер счета введен верно')
        return f"**{number_encoder[16:21]}"
    if len(number_encoder) != 20:
        logger.error('Номер счета введен не верно')
        return "Номер счета введен неверно"
