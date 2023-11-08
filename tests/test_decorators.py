from typing import Any
import pytest
from src.decorators import log, my_function
import datetime


@pytest.fixture(params=[10.5, 20, -30])
def number_one(request) -> int:
    return request.param


@pytest.fixture(params=[5, 9, 0])
def number_two(request) -> int:
    return request.param


@log(filename='nn_.txt')
def test_my_function(number_one: int, number_two: int) -> None:
    assert my_function(number_one, number_two) == 'Файл создан'


@log(filename='_.txt')
def test_my_function_none_filename(number_one: int, number_two: int) -> None:
    assert my_function(number_one, number_two) == (f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, "
                                                   f"my_function, ok")
