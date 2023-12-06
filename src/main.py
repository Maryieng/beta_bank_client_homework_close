import json
import math
from pprint import pprint

from src.generators import filter_by_currency
from src.processing import list_dictionaries_with_key, sorted_list_of_dict
from src.reading_data import reading_data_from_file_csv, reading_data_from_file_xlsx, searching_data_by_string
from src.utils import getting_data_from_file
from src.widget import convert_to_date, mask_with_card_type

choice_user = int(input("""Привет! Добро пожаловать в программу работы с банковскими транзакициями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла
"""))
if choice_user == 1:
    print("Для обработки выбран json файл.")
    file_user = getting_data_from_file('operations.json')
elif choice_user == 2:
    print("Для обработки выбран csv файл.")
    line_file = reading_data_from_file_csv('transactions.csv')
    file_intermediate = json.loads(json.dumps(list(line_file.T.to_dict().values())))
    file_user = []
    for source_dict in file_intermediate:
        keys, values = list(source_dict.keys())[0].split(';'), list(source_dict.values())[0].split(';')
        new_dict = {
            'id': int(values[0]) if values[0] else 0,
            'state': values[1],
            'date': values[2],
            'operationAmount': {
                'amount': values[3],
                'currency': {
                    'name': values[4],
                    'code': values[5]
                }
            },
            'description': values[8] if values[8] else '',
            'from': values[6],
            'to': values[7]
        }
        file_user.append(new_dict)
elif choice_user == 3:
    print("Для обработки выбран xlsx файл.")
    line_file = reading_data_from_file_xlsx('transactions_excel.xlsx')
    file_intermediate = json.loads(json.dumps(list(line_file.T.to_dict().values())))
    file_user = []

    for item in file_intermediate:
        new_item = {
            "id": int(item['id']) if not math.isnan(item['id']) else None,
            "state": item['state'],
            "date": str(item['date']).split('T')[0],
            "operationAmount": {
                "amount": float(item['amount']),
                "currency": {
                    "name": item['currency_name'],
                    "code": item['currency_code']
                }
            },
            "description": item['description'],
            "from": str(item['from']),
            "to": str(item['to'])
        }
        file_user.append(new_item)

else:
    print("Ошибка выбора")

while True:
    user_operations = input("""Введите статус по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()
    if user_operations == 'EXECUTED' or user_operations == 'CANCELED' or user_operations == 'PENDING':
        print(f"""Операции отфильтрованы по статусу {user_operations}""")
        list_operations_by_status = list_dictionaries_with_key(file_user)
        break
    else:
        print(f"Статус операции {user_operations} недоступен")


operations_date_user = input("""Отсортировать операции по дате? Да/Нет
""").lower()
if operations_date_user == "да":
    sorting_user = input("""Отсортировать по возрастанию или по убыванию?
""").lower()
    if sorting_user == "по возрастанию":
        sorted_list = sorted_list_of_dict(list_operations_by_status, False)
    else:
        sorted_list = sorted_list_of_dict(list_operations_by_status, True)
else:
    sorted_list = list_operations_by_status

currency_user = input("""Выводить только рублевые тразакции? Да/Нет
""").lower()
if currency_user == "да":
    sort_by_currency = filter_by_currency(sorted_list, 'RUB')
else:
    sort_by_currency = sorted_list
selection_word_user = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет
""").lower()
if selection_word_user == "да":
    user_word = input("""Введите слово/строку по которой необходимо отфильтровать
    """).lower()
    filter_by_word = searching_data_by_string(sort_by_currency, user_word)
else:
    filter_by_word = sort_by_currency
print(f"""Распечатываю итоговый список транзакций...
Всего банковских операций в выборке: {len(filter_by_word)}""")
print(filter_by_word)
if len(filter_by_word) == 0:
    pprint('Не найдено ни одной транзакции подходящей под ваши условия фильтрации')
else:
    for operation in filter_by_word:
        print(f"""{convert_to_date(operation['date'])} {operation['description']}
{mask_with_card_type(operation.get('from'))} -> {mask_with_card_type(operation.get('to'))}
Сумма: {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['code']}.
""")
