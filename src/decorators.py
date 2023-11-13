import datetime
from functools import wraps
from typing import Any, Callable


def log(filename=None) -> Any:
    """ логирует вызов функции и ее результат в файл или в консоль. необязательный аргумент filename,
    который определяет имя файла, в который будут записываться логи. Если
    filename не задан, то логи будут выводиться в консоль """
    def wrapped(function: Callable) -> Any:
        @wraps(function)
        def inner(*args: int) -> Any:
            try:
                result = function(*args)
                message = f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, {function.__name__}, ok"
                print(message)
                if filename:
                    with open(filename, "w") as file:
                        file.write(message + "\n")
            except Exception as e:
                message_error = (f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, "
                                 f"Возникла ошибка:{str(e)}. {function.__name__}, Inputs: {args}\n")
                print(message_error)
                if filename:
                    with open(filename, "a") as file:
                        file.write(message_error + "\n")
                    raise e
            return result
        return inner
    return wrapped
