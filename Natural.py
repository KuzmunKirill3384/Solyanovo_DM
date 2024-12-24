from __future__ import annotations


class Natural:
    def __init__(self, value) -> None:
        # Конструктор принимает строку, представляющую число,
        # и инициализирует его в реверсированном виде для удобства обработки.
        self.data = [int(digit) for digit in value[::-1]]
        self.length = len(self.data)

    @classmethod
    def copy(cls, value) -> Natural:
        # Создает новый экземпляр класса Natural, копируя данные из существующего экземпляра.
        instance = cls.__new__(cls)
        instance.data = value.data[:]
        instance.length = value.length
        return instance

    def __eq__(self, value) -> bool:
        # Проверяет, равны ли два объекта типа Natural.
        if self is value:
            return True
        if self.length != value.length:
            return False
        for i in range(self.length):
            if self.data[i] != value.data[i]:
                return False
        return True

    def __ne__(self, value) -> bool:
        # Проверяет, не равны ли два объекта типа Natural.
        return not (self == value)

    def __lt__(self, value) -> bool:
        # Сравнивает текущий объект с другим на меньше.
        if self.length > value.length:
            return False
        if self.length < value.length:
            return True
        for i in range(self.length - 1, -1, -1):
            if self.data[i] != value.data[i]:
                return self.data[i] < value.data[i]
        return False

    def __le__(self, value) -> bool:
        # Проверяет, меньше ли или равно значение текущего объекта другому.
        return (self < value) or (self == value)

    def __gt__(self, value) -> bool:
        # Проверяет, больше ли значение текущего объекта другого.
        return not (self <= value)

    def __ge__(self, value) -> bool:
        # Проверяет, больше ли или равно значение текущего объекта другому.
        return not (self < value)

    def COM_NN_D(self, value) -> int:
        # Сравнивает два объекта Natural и возвращает результат:
        # 1, если self меньше, 2, если self больше, 0, если равны.
        if self > value:
            return 2
        elif self < value:
            return 1
        else:
            return 0

    def NZER_N_B(self) -> int:
        # Проверяет, является ли число ненулевым.
        # Возвращает 1, если это так, и 0, если это ноль.
        return 1 if (self.length != 1 or self.data[0] != 0) else 0

    def ADD_1N_N(self) -> Natural:
        # Добавляет 1 к текущему числу и возвращает результат.
        i = 0
        while i < self.length and self.data[i] == 9:
            self.data[i] = 0
            i += 1
        if i == self.length:
            self.length += 1
            self.data.append(1)  # Добавляем новую цифру, если мы переполнили
        else:
            self.data[i] += 1
        return self

    def ADD_NN_N(self, value) -> Natural:
        # Складывает текущее число с другим числом и возвращает результат.
        max_length = max(self.length, value.length)
        carry = 0
        result_data = []

        for i in range(max_length):
            digit1 = self.data[i] if i < self.length else 0
            digit2 = value.data[i] if i < value.length else 0
            total = digit1 + digit2 + carry
            result_data.append(total % 10)  # Получаем последнюю цифру
            carry = total // 10  # Обновляем значение переноса

        if carry:
            result_data.append(carry)  # Добавляем остаток, если он есть

        # Создаем новый объект Natural для результата
        result = Natural(''.join(map(str, result_data[::-1])))
        return result

    def SUB_NN_N(self, value) -> Natural:
        # Вычитает одно Natural число из другого. Если результат отрицательный, вызывает ошибку.
        comparison = self.COM_NN_D(value)
        if comparison == 1:
            raise ValueError("Результат вычитания будет отрицательным")

        result_data = []
        borrow = 0
        max_length = max(self.length, value.length)

        for i in range(max_length):
            digit1 = self.data[i] if i < self.length else 0
            digit2 = value.data[i] if i < value.length else 0

            if digit1 < digit2 + borrow:
                digit1 += 10  # Заимствование
                current_result = digit1 - digit2 - borrow
                borrow = 1  # Заем для следующего разряда
            else:
                current_result = digit1 - digit2 - borrow
                borrow = 0

            result_data.append(current_result)

        # Удаляем ведущие нули из результата
        while result_data and result_data[-1] == 0:
            result_data.pop()

        result = Natural(''.join(map(str, result_data[::-1])))
        return result

    def MUL_ND_N(self, digit) -> Natural:
        # Умножает текущее число на одну цифру (от 0 до 9).
        if not (0 <= digit <= 9):
            raise ValueError("Цифра должна быть в диапазоне от 0 до 9")

        carry = 0  # Для хранения переноса
        result_data = []

        for i in range(self.length):
            current_product = self.data[i] * digit + carry
            result_data.append(current_product % 10)  # Сохраняем последнюю цифру
            carry = current_product // 10  # Рассчитываем новый перенос

        while carry:
            result_data.append(carry % 10)
            carry //= 10

        return Natural(''.join(map(str, result_data[::-1])))

    def MUL_Nk_N(self, k) -> Natural:
        # Умножает текущее число на 10 в степени k (сдвигает на k позиций влево).
        result = Natural.copy(self)
        result.data.reverse()
        for i in range(k):
            result.data.append(0)
            result.length += 1
        result.data.reverse()
        return result

    def MUL_NN_N(self, value) -> Natural:
        # Умножает текущее число на другое число и возвращает результат.
        result = Natural('0')  # Начинаем с 0
        for i, digit in enumerate(value.data):  # Используем enumerate для получения индекса и цифры
            if digit == 0:
                continue  # Пропускаем, если цифра 0
            # Умножаем текущее число на цифру
            partial_product = self.MUL_ND_N(digit)
            # Сдвигаем результат влево на i позиций
            partial_product = partial_product.MUL_Nk_N(i)
            # Складываем с итоговым результатом
            result = result.ADD_NN_N(partial_product)
        return result

    def SUB_NDN_N(self, value, k) -> Natural:
        # Вычитает k-кратное значение другого Natural числа из текущего.
        um = Natural.copy(self)
        vc = Natural.copy(value.MUL_ND_N(k))
        result = um.COM_NN_D(vc)
        if result == 2:
            return um.SUB_NN_N(vc)
        if result == 1:
            raise ValueError("Результат вычитания будет отрицательным")
        return Natural('0')

    def DIV_NN_Dk(self, value) -> Natural:
        # Делит текущее число на число, возвращая максимальный k, для которого деление возможно.
        if not self.NZER_N_B() or not value.NZER_N_B():
            return Natural("0")
        if self.COM_NN_D(value) == 2 or self.COM_NN_D(value) == 0:
            larger = self
            smaller = value
        else:
            raise ValueError("Ошибка: деление на большее число")  # оги могут быть равны, пофиксить

        k = 1
        while larger.COM_NN_D(smaller.MUL_Nk_N(k)) == 2 or larger.COM_NN_D(smaller.MUL_Nk_N(k)) == 0:
            k += 1
        k -= 1
        smaller = smaller.MUL_Nk_N(k)
        first_digit = Natural('0')
        while larger.COM_NN_D(smaller) == 2 or larger.COM_NN_D(smaller) == 0:
            larger = larger.SUB_NN_N(smaller)
            first_digit.ADD_1N_N()
        return first_digit.MUL_Nk_N(k)

    def DIV_NN_N(self, value) -> Natural:
        # Делит одно число на другое и возвращает результат.
        if (self.NZER_N_B() == False or value.NZER_N_B() == False):
            return Natural("0")

        result = Natural("0")
        first = Natural.copy(self)
        second = Natural.copy(value)

        while first >= second:
            digit = first.DIV_NN_Dk(second)
            first = first.SUB_NN_N(digit.MUL_NN_N(second))
            result = result.ADD_NN_N(digit)
        return result

    def MOD_NN_N(self, value) -> Natural:
        # Возвращает остаток от деления текущего числа на другое.
        if str(self.SUB_NN_N(self.DIV_NN_N(value).MUL_NN_N(value))) == '':
            return Natural("0")
        return self.SUB_NN_N(self.DIV_NN_N(value).MUL_NN_N(value))

    def GCF_NN_N(self, value: Natural) -> Natural:
        if self.NZER_N_B() and value.NZER_N_B():
            a = Natural.copy(self)
            b = Natural.copy(value)
            while b.NZER_N_B():
                a, b = b, a.MOD_NN_N(b)  # Присваиваем b = a % b

            return a
        return Natural('0')  # НОД(0, x) = x

    def LCM_NN_N(self, value: Natural) -> Natural:
        return self.MUL_NN_N(value).DIV_NN_N(self.GCF_NN_N(value))

    def __str__(self):
        # Представляет число в виде строки.
        return ''.join(str(digit) for digit in self.data[::-1])
