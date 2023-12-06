from src.masks import account_number_encoder, card_number_encoder


def mask_with_card_type(number_object: str) -> str:
    """ Функция принимает номер и тип карты/счета и возвращает в виде:
     "Visa Platinum 7000 79** **** 6361 / Счет **4305" """
    try:
        number_object_list = number_object.split()
        if "чет" in number_object:
            return f'{number_object_list[0].title()} {account_number_encoder(number_object_list[1])}'
        elif 'nan' in number_object:
            return 'Неизвестно'
        elif number_object_list[1].isalpha():
            return (f'{number_object_list[0].title()} {number_object_list[1].title()} '
                    f'{card_number_encoder(number_object_list[2])}')
        else:
            return f'{number_object_list[0].title()} {card_number_encoder(number_object_list[1])}'
    except Exception:
        return 'Неизвестно'


def convert_to_date(string: str) -> str:
    """ Функция принимает строку и возвращает в виде: "11.07.2018" """
    return f'{string[8:10]}.{string[5:7]}.{string[0:4]}'
