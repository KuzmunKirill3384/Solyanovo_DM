import time
from Rational import Rational
from Polynom import Polynom


def test_polynom_operations():
    # Тестирование создания полиномов
    def test_create_polynom():
        parts = [Rational("1", "1"), Rational("2", "1"), Rational("3", "1")]
        start_time = time.time()
        polynom = Polynom(parts)
        result = str(polynom)
        end_time = time.time()
        print(f"test_create_polynom: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование сложения полиномов
    def test_addition():
        p1 = Polynom([Rational("1", "1"), Rational("2", "1"), Rational("2", "1")])
        p2 = Polynom([Rational("0", "1"), Rational("1", "1"), Rational("1", "1")])
        start_time = time.time()
        result = p1.ADD_PP_P(p2)
        end_time = time.time()
        print(f"test_addition: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование вычитания полиномов
    def test_subtraction():
        p1 = Polynom([Rational("3", "1"), Rational("4", "1"), Rational("5", "1")])
        p2 = Polynom([Rational("1", "1"), Rational("2", "1"), Rational("1", "1")])
        start_time = time.time()
        result = p1.SUB_PP_P(p2)
        end_time = time.time()
        print(f"test_subtraction: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование умножения полиномов
    def test_multiplication():
        p1 = Polynom([Rational("1", "1"), Rational("0", "1"), Rational("2", "1")])
        p2 = Polynom([Rational("1", "1"), Rational("1", "1")])
        start_time = time.time()
        result = p1.MUL_PP_P(p2)
        end_time = time.time()
        print(f"test_multiplication: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование умножения полинома на рациональное число
    def test_multiply_polynomial_by_rational():
        p = Polynom([Rational("1", "1"), Rational("2", "1")])
        r = Rational("3", "1")
        start_time = time.time()
        result = p.MUL_PQ_P(r)
        end_time = time.time()
        print(f"test_multiply_polynomial_by_rational: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование деления полиномов
    def test_division():
        p1 = Polynom([Rational("1", "1"), Rational("2", "1"), Rational("1", "1")])
        p2 = Polynom([Rational("1", "1"), Rational("1", "1")])
        start_time = time.time()
        result = p1.DIV_PP_P(p2)
        end_time = time.time()
        print(f"test_division: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование вычисления остатка от деления полиномов
    def test_modulus():
        p1 = Polynom([Rational("1", "1"), Rational("2", "1"), Rational("1", "1")])
        p2 = Polynom([Rational("1", "1"), Rational("1", "1")])
        start_time = time.time()
        result = p1.MOD_PP_P(p2)
        end_time = time.time()
        print(f"test_modulus: полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование нахождения производной
    def test_derivative():
        p = Polynom([Rational("3", "1"), Rational("2", "1"), Rational("1", "1")])
        start_time = time.time()
        result = p.DER_P_P()
        end_time = time.time()
        print(f"test_derivative: полученный: {result}, время: {end_time - start_time:.10f}")

    test_create_polynom()
    print()
    test_addition()
    print()
    test_subtraction()
    print()
    test_multiplication()
    print()
    test_multiply_polynomial_by_rational()
    print()
    test_division()
    print()
    test_modulus()
    print()
    test_derivative()
    print()



# Запуск всех тестов
test_polynom_operations()