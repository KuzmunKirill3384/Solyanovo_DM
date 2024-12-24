import time
from Natural import Natural
from Integer import Integer


def test_integer_operations():
    # Тестирование создания целых чисел
    def test_create_integer():
        s = "123"
        expected = "123"
        start_time = time.time()
        integer = Integer(s)
        result = str(integer)
        end_time = time.time()
        print(f"test_create_integer: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    def test_create_negative_integer():
        s = "-456"
        expected = "-456"
        start_time = time.time()
        integer = Integer(s)
        result = str(integer)
        end_time = time.time()
        print(
            f"test_create_negative_integer: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование сложения целых чисел
    def test_addition():
        a = Integer("123")
        b = Integer("456")
        expected = "579"
        start_time = time.time()
        result = a.ADD_ZZ_Z(b)
        end_time = time.time()
        print(f"test_addition: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Integer("123")
        b = Integer("-130")
        expected = "-7"
        start_time = time.time()
        result = a.ADD_ZZ_Z(b)
        end_time = time.time()
        print(
            f"test_addition_with_negative: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование вычитания целых чисел
    def test_subtraction():
        a = Integer("456")
        b = Integer("123")
        expected = "333"
        start_time = time.time()
        result = a.SUB_ZZ_Z(b)
        end_time = time.time()
        print(f"test_subtraction: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Integer("-123")
        b = Integer("456")
        expected = "-579"
        start_time = time.time()
        result = a.SUB_ZZ_Z(b)
        end_time = time.time()
        print(
            f"test_subtraction_negative_result: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование умножения целых чисел
    def test_multiplication():
        a = Integer("12")
        b = Integer("10")
        expected = "120"
        start_time = time.time()
        result = a.MUL_ZZ_Z(b)
        end_time = time.time()
        print(f"test_multiplication: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Integer("-12")
        b = Integer("10")
        expected = "-120"
        start_time = time.time()
        result = a.MUL_ZZ_Z(b)
        end_time = time.time()
        print(
            f"test_multiplication_negative: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование деления целых чисел
    def test_division():
        a = Integer("120")
        b = Integer("10")
        expected = "12"
        start_time = time.time()
        result = a.DIV_ZZ_Z(b)
        end_time = time.time()
        print(f"test_division: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Integer("-120")
        b = Integer("10")
        expected = "-12"
        start_time = time.time()
        result = a.DIV_ZZ_Z(b)
        end_time = time.time()
        print(
            f"test_division_with_negative: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Integer("120")
        b = Integer("0")
        expected = "0"  # Ожидаем пустой объект, без конкретного значения
        start_time = time.time()
        result = a.DIV_ZZ_Z(b)
        end_time = time.time()
        print(
            f"test_division_by_zero: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование остатка от деления
    def test_modulus():
        a = Integer("123")
        b = Integer("10")
        expected = "3"
        start_time = time.time()
        result = a.MOD_ZZ_Z(b)
        end_time = time.time()
        print(f"test_modulus: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Integer("-123")
        b = Integer("10")
        expected = "7"
        start_time = time.time()
        result = a.MOD_ZZ_Z(b)
        end_time = time.time()
        print(
            f"test_modulus_with_negative: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Запуск тестов
    test_create_integer()
    print()
    test_create_negative_integer()
    print()
    test_addition()
    print()
    test_subtraction()
    print()
    test_multiplication()
    print()
    test_division()
    print()
    test_modulus()


# Запуск всех тестов
test_integer_operations()
