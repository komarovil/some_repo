
def test_division_2_1(div_2):
    '''
    1.Проверка на корректное деление кратных чисел
    :param div_2: fixture
    :return:
    '''
    assert div_2(4, 1) == 0


def test_division_2_2(div_2):
    '''
    2.Проверка на корректное деление не кратных чисел
    :param div_2: fixture
    :return:
    '''
    assert div_2(5, 2) == 1


def test_division_2_3(div_2):
    '''
    3.Проверка на корректное деление при дробных числах
    :param div_2: fixture
    :return:
    '''
    assert type(div_2(4.2 , 3)) is float