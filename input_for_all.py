from Natural import Natural
from Integer import Integer
from Rational import Rational
from Polynom import Polynom

def input_natural():
    print("Введите натуральное число:", end=' ')
    data = input()
    return create_natural(data)


def create_natural(data):
    from Natural import Natural
    return Natural(data)


def input_integer():
    print("Введите целое число:", end=' ')
    data = input()
    return create_integer(data)


def create_integer(data):
    return Integer(data)


def input_rational():
    print("Введите дробь в формате x/y, где числитель - целое, знаменатель натуральное.")
    numerator, denominator = input().split('/')
    return create_rational(create_integer(numerator), create_natural(denominator))


def create_rational(numerator, denominator):
    return Rational(numerator, denominator)

def input_polynomial():
    mas = input("Введите коэффициенты  вашего многочлена через пробел: ").split()
    data = []
    for i in mas:
        numerator, denominator = i.split('/')
        data.append(create_rational(numerator, denominator))
    return Polynom(data[::-1])
