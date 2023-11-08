import datetime
from functools import wraps
from typing import Any, Callable


def log(filename='_.txt') -> Any:
    """ логирует вызов функции и ее результат в файл или в консоль. необязательный аргумент filename,
    который определяет имя файла, в который будут записываться логи. Если
    filename не задан, то логи будут выводиться в консоль """
    def wrapped(function: Callable):
        @wraps(function)
        def inner(*args, **kwargs):
            now = datetime.datetime.now()
            try:
                _ = function(*args, **kwargs)
                message = f"{now.strftime('%d-%m-%Y %H:%M:%S')}, {function.__name__}, ok\n"
            except Exception as e:
                _ = f"error: {str(e)}"
                message = (f"{now.strftime('%d-%m-%Y %H:%M:%S')}, {function.__name__}, "
                           f"error: {str(e)}, Inputs: {args, kwargs}\n")
            if filename == '_.txt':
                return message
            else:
                with open(filename, 'w+') as file:
                    file.write(message)
                return "Файл создан"
        return inner
    return wrapped


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y
