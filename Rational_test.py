import time
from Natural import Natural
from Integer import Integer
from Rational import Rational


def test_rational_operations():
    # Тестирование создания дробей
    def test_create_rational():
        num, denum = "3", "4"
        expected = "3/4"
        start_time = time.time()
        rational = Rational(num, denum)
        result = str(rational)
        end_time = time.time()
        print(f"test_create_rational: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")



    # Тестирование сложения дробей
    def test_addition():
        a = Rational("1", "2")
        b = Rational("1", "3")
        expected = "5/6"
        start_time = time.time()
        result = a.ADD_QQ_Q(b)
        end_time = time.time()
        print(f"test_addition: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Rational("2", "3")
        b = Rational("4", "3")
        expected = "2/1"  # Это 2
        start_time = time.time()
        result = a.ADD_QQ_Q(b)
        end_time = time.time()
        print(
            f"test_addition_with_same_denominator: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование вычитания дробей
    def test_subtraction():
        a = Rational("3", "4")
        b = Rational("1", "2")
        expected = "1/4"
        start_time = time.time()
        result = a.SUB_QQ_Q(b)
        end_time = time.time()
        print(f"test_subtraction: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Rational("1", "2")
        b = Rational("3", "4")
        expected = "-1/4"
        start_time = time.time()
        result = a.SUB_QQ_Q(b)
        end_time = time.time()
        print(
            f"test_subtraction_negative_result: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование умножения дробей
    def test_multiplication():
        a = Rational("1", "4")
        b = Rational("1", "2")
        expected = "1/8"
        start_time = time.time()
        result = a.MUL_QQ_Q(b)
        end_time = time.time()
        print(f"test_multiplication: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Rational("0", "1")
        b = Rational("4", "5")
        expected = "0/1"  # Умножение на 0
        start_time = time.time()
        result = a.MUL_QQ_Q(b)
        end_time = time.time()
        print(
            f"test_multiplication_zero: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование деления дробей
    def test_division():
        a = Rational("1", "2")
        b = Rational("1", "3")
        expected = "3/2"
        start_time = time.time()
        result = a.DIV_QQ_Q(b)
        end_time = time.time()
        print(f"test_division: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        '''a = Rational("1", "4")
        b = Rational("0", "1")
        expected = "0/1"  # Ожидаем обработку деления на 0
        start_time = time.time()
        result = a.DIV_QQ_Q(b)  # Обработка деления на ноль
        end_time = time.time()
        print(f"test_division_by_zero: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")'''

    # Тестирование равенства дробей
    def test_equality():
        a = Rational("1", "2")
        b = Rational("2", "4")
        expected = True
        start_time = time.time()
        end_time = time.time()
        print(f"test_equality: ожидаемый: {expected}, полученный: {a==b}, время: {end_time - start_time:.10f}")

        a = Rational("1", "2")
        b = Rational("1", "3")
        expected = False
        start_time = time.time()
        result = a == b
        end_time = time.time()
        print(f"test_equality_false: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Запуск тестов
    test_create_rational()
    print()
    test_addition()
    print()
    test_subtraction()
    print()
    test_multiplication()
    print()
    test_division()
    print()
    test_equality()


# Запуск всех тестов
test_rational_operations()
