from functools import wraps
from typing import Callable, Any
import datetime

def log(filename='_.txt') -> Any:
    def wrapped(function: Callable):
        @wraps(function)
        def inner(*args, **kwargs):
            now = datetime.datetime.now()
            try:
                result = function(*args, **kwargs)
                message = f"{now.strftime('%d-%m-%Y %H:%M:%S')}, {function.__name__}, ok\n"
            except Exception as e:
                result = f"error: {str(e)}"
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


@log(filename='_.txt')
def my_function(x: int, y: int) -> int:
    return x / y

print(my_function(4,2))