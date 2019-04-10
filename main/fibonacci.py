
class FibonnaciNumbers(object):


    def __init__(self, limit):
        self.limit = limit


    def sum_fibonacci(limit):
        '''
        Сумма первых чисел чисел Фиббоначи до указанного числа
        :param limit: кол-во первых числе Фиббоначи
        :return: сумму
        '''
        a = 1
        b = 1
        sum = 1
        cont = 1
        while cont < limit:
            sum += b
            a, b = b, a+b
            cont += 1

        return sum