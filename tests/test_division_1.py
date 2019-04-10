import pytest

def test_division_1_1(div_1, some_function):
    '''
    1.Проверка на вывод 1  при a = b (True)
    :param div_1: fixture
    :return:
    '''
    assert div_1(4, 4) == 1


def test_division_1_2(div_1):
    '''
    2.Проверка деления отрцательных простых чисел (True)
    :param div_1: fixture
    :return:
    '''
    assert div_1(-4, 1) == -4


def test_division_1_3(div_1):
    '''
    3.Проверка деления на ноль (False)
    :param div_1: fixture
    :return:
    '''
    with pytest.raises(ZeroDivisionError):
        div_1(4, 0)


def test_division_1_4(div_1):
    '''
    4. Проверка передачу неизвестной переменной (False name)
    :param div_1: fixture
    :return:
    '''
    with pytest.raises(NameError):
        div_1(f, 4)


def test_division_1_5(div_1):
    '''
    5.Проверка вывода дробного числа при делении с дробной переменной a or b (True )
    :param div_1: fixture
    :return:
    '''
    assert type(div_1(4.0, 1)) is float


def test_division_1_6(div_1):
    '''
    6. Проверка вывода 0 при a < b
    :param div_1: fixture
    :return:
    '''
    assert div_1(1, 2) == 0


def test_division_1_7(div_1):
    '''
    7.Проверка на a or b = str
    :param div_1: fixture
    :return:
    '''
    with pytest.raises(TypeError):
        div_1('2', 2)


def test_division_1_8(div_1):
    '''
    8.Проверка на вывод целого числа при при a > b (True)
    :param div_1: fixture
    :return:
    '''
    assert type(div_1(4, 2)) is int