import datetime

from src.decorators import log


def test_log_to_file() -> None:
    filename = "test_logs.txt"
    @log(filename=filename)
    def my_function(param1: int, param2: int) -> int:
        return param1 + param2

    my_function(10, 2)

    with open(filename, 'r') as file:
        logs = file.read()
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    expected_logs = f"{now}, my_function, ok\n"
    assert logs == expected_logs


@log()
def test_console() -> None:
    def my_function(param1: int, param2: int) -> float:
        return param1 / param2

    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    assert my_function(10, 0) == f'{now}, Возникла ошибка:division by zero. my_function, Inputs: (10, 0)'
    assert my_function(10, 5) == f'{now}, my_function, ok\n'
