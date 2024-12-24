import time
from Natural import Natural

def test_natural_operations():
    # Тестирование создания натуральных чисел
    def test_create_natural():
        s = "123"
        expected = "123"
        start_time = time.time()
        natural = Natural(s)
        result = str(natural)
        end_time = time.time()
        print(f"test_create_natural: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    def test_create_zero_natural():
        s = "0"
        expected = "0"
        start_time = time.time()
        natural = Natural(s)
        result = str(natural)
        end_time = time.time()
        print(f"test_create_zero_natural: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование сложения натуральных чисел
    def test_addition():
        a = Natural("123")
        b = Natural("456")
        expected = "579"
        start_time = time.time()
        result = a.ADD_NN_N(b)
        end_time = time.time()
        print(f"test_addition: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Natural("999")
        b = Natural("1")
        expected = "1000"
        start_time = time.time()
        result = a.ADD_NN_N(b)
        end_time = time.time()
        print(f"test_addition_carry: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование вычитания натуральных чисел
    def test_subtraction():
        a = Natural("456")
        b = Natural("123")
        expected = "333"
        start_time = time.time()
        result = a.SUB_NN_N(b)
        end_time = time.time()
        print(f"test_subtraction: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Natural("1000")
        b = Natural("999")
        expected = "1"
        start_time = time.time()
        result = a.SUB_NN_N(b)
        end_time = time.time()
        print(f"test_subtraction_result: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        try:
            a = Natural("123")
            b = Natural("456")
            result = a.SUB_NN_N(b)
        except ValueError as e:
            print(f"test_subtraction_negative_result: ожидается ошибка: {str(e)}")

    # Тестирование умножения натуральных чисел
    def test_multiplication():
        a = Natural("12")
        b = Natural("10")
        expected = "120"
        start_time = time.time()
        result = a.MUL_NN_N(b)
        end_time = time.time()
        print(f"test_multiplication: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Natural("999")
        b = Natural("1")
        expected = "999"
        start_time = time.time()
        result = a.MUL_NN_N(b)
        end_time = time.time()
        print(f"test_multiplication_identity: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Тестирование деления натуральных чисел
    def test_division():
        a = Natural("120")
        b = Natural("10")
        expected = "12"
        start_time = time.time()
        result = a.DIV_NN_N(b)
        end_time = time.time()
        print(f"test_division: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Natural("10")
        b = Natural("2")
        expected = "5"
        start_time = time.time()
        result = a.DIV_NN_N(b)
        end_time = time.time()
        print(f"test_division_even: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        try:
            a = Natural("120")
            b = Natural("0")
            result = a.DIV_NN_N(b)
        except ValueError as e:
            print(f"test_division_by_zero: ожидается ошибка: {str(e)}")

    # Тестирование остатка от деления
    def test_modulus():
        a = Natural("123")
        b = Natural("10")
        expected = "3"
        start_time = time.time()
        result = a.MOD_NN_N(b)
        end_time = time.time()
        print(f"test_modulus: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

        a = Natural("100")
        b = Natural("100")
        expected = "0"
        start_time = time.time()
        result = a.MOD_NN_N(b)
        end_time = time.time()
        print(f"test_modulus_zero: ожидаемый: {expected}, полученный: {result}, время: {end_time - start_time:.10f}")

    # Запуск тестов
    test_create_natural()
    print()
    test_create_zero_natural()
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
test_natural_operations()