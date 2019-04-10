import pytest


from main.fibonacci import FibonnaciNumbers
from main.division import division_1
from main.division import division_2

####################################
@pytest.fixture(scope='session')
def some_function():
    """
    Фикстура для выводы Start и End в начале и конце тестов. Scope = session. Определена в test_division_1
    :return:
    """
    print('\nStart test')
    yield division_1
    print ('\nEnd test')

@pytest.fixture(scope='function')
def div_1():
    """
    Фикстура для первой функции
    :return:
    """
    print ('\nThis is test the firs function')
    yield division_1
    print('\nThis firs function is success')

####################################


@pytest.fixture(scope='module')
def div_2():
    """
    Фикстура для второй функции
    :return:
    """
    print ('\nThis test is the second function stack.')
    yield division_2
    print ('\nThis test of the second  stack is success')


####################################


@pytest.fixture(scope='function')
def fibonacci():
    """
    Фикстура для функции Фибоначи
    :return:
    """
    print('\nThis is test the third function')
    yield FibonnaciNumbers.sum_fibonacci
    print('\nThis third function is success')


####################################