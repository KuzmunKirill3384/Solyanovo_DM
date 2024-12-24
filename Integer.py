from Natural import Natural


class Integer:

    def __init__(self, s):
        self.sign = 0  # 0 - положительное, 1 - отрицательное
        self.number = Natural("")  # По умолчанию - ноль
        if s == "":
            return
        if s[0] == "-":
            self.sign = 1  # Отрицательное число
            s = s[1:]
        try:
            self.number = Natural(s)  # Инициализация натурального числа
        except:
            self.number = Natural("")  # При ошибке создаётся пустой объект

    def __str__(self):
        out = ''.join([str(i) for i in self.number.data[::-1]])
        return f'-{out}' if self.sign == 1 else out

    def __eq__(self, value) -> bool:
        # Проверяет, равны ли два объекта типа Interer.
        if self.sign != value.sign:
            return False
        else:
            if self.number == value.number:
                return True
            else:
                return False

    def __gt__(self, other):
        # Если знаки различаются, то определяем большее число по знакам
        if self.sign != other.sign:
            # Если текущее число положительное, а другое - отрицательное
            return self.sign == 0
        else:
            # Если знаки равны, сравниваем модуль чисел
            if self.sign == 0:  # Оба числа неотрицательные
                return self.number.COM_NN_D(other.number) == 2  # Если self > other
            else:  # Оба числа отрицательные
                return self.number.COM_NN_D(other.number) == 1  # Если self < other

    @staticmethod
    def copy(x):
        res = Integer("")  # Пустой объект
        res.sign = x.sign  # Копируем знак
        res.number = Natural.copy(x.number)  # Копируем число
        return res

    def ABS_Z_N(self):
        return Natural.copy(self.number)  # Модуль числа

    def POZ_Z_D(self):
        if self.number.length == 1 and self.number.data[0] == 0:
            return 0  # Ноль
        return 2 if self.sign == 0 else 1  # Положительное или отрицательное

    def MUL_ZM_Z(self):
        res = Integer.copy(self)  # Копия числа
        if res.number.length == 1 and res.number.data[0] == 0:
            return res  # Ноль остается нулем
        res.sign = 1 - res.sign  # Изменяем знак
        return res

    @staticmethod
    def TRANS_N_Z(x):
        res = Integer("")  # Пустой объект
        res.sign = 0  # Положительное
        res.number = Natural.copy(x)  # Копия натурального числа
        return res

    def TRANS_Z_N(self):
        return Natural.copy(self.number) if self.sign == 0 else Natural("")  # Конвертация в натуральное

    def ADD_ZZ_Z(self, other):
        res = Integer("")  # Пустой объект
        if self.sign == other.sign:
            res.sign = self.sign
            res.number = self.number.ADD_NN_N(other.number)  # Сложение
        else:
            comp = self.number.COM_NN_D(other.number)
            if comp == 2:
                res.sign = self.sign
                res.number = self.number.SUB_NN_N(other.number)  # Вычитание
            elif comp == 1:
                res.sign = other.sign
                res.number = other.number.SUB_NN_N(self.number)
            else:
                res.sign = 0
                res.number = Natural("0")  # Результат ноль
        return res

    def SUB_ZZ_Z(self, other):
        res = Integer("")  # Пустой объект
        if self.sign == other.sign:
            if self.number.COM_NN_D(other.number) == 2:
                res.sign = self.sign
                res.number = self.number.SUB_NN_N(other.number)  # Вычитание
            elif self.number.COM_NN_D(other.number) == 1:
                res.sign = 1 - self.sign
                res.number = other.number.SUB_NN_N(self.number)
            else:
                res.sign = 0
                res.number = Natural("0")  # Результат ноль
        else:
            res.sign = self.sign
            res.number = self.number.ADD_NN_N(other.number)  # Сложение
        return res

    def MUL_ZZ_Z(self, other):
        res = Integer("")  # Пустой объект
        if (self.number.length == 1 and self.number.data[0] == 0) or (
                other.number.length == 1 and other.number.data[0] == 0):
            return res  # Результат ноль
        res.sign = 0 if (self.sign == other.sign) else 1  # Определяем знак
        res.number = self.number.MUL_NN_N(other.number)  # Умножение
        return res

    def DIV_ZZ_Z(self, other):
        res = Integer("")  # Пустой объект
        if other.number.length == 1 and other.number.data[0] == 0:
            return res  # Деление на ноль
        res.number = self.number.DIV_NN_N(other.number)  # Деление

        if self.sign != other.sign and (
                self.number.MOD_NN_N(other.number).length > 1 or self.number.MOD_NN_N(other.number).data[0] != 0):
            res.number = res.number.ADD_1N_N()  # Добавляем единицу к частному
        res.sign = 1 if (self.sign != other.sign) else 0  # Знак частного
        return res

    def MOD_ZZ_Z(self, other):
        res = Integer("")  # Пустой объект
        if other.number.length == 1 and other.number.data[0] == 0:
            return res  # Деление на ноль
        res.sign = 0  # Остаток положительный
        res.number = self.number.MOD_NN_N(other.number)  # Остаток от деления

        if res.number.length > 1 or res.number.data[0] != 0:
            if self.sign == 1 or other.sign == 1:
                res.number = other.number.SUB_NN_N(res.number)  # Коррекция остатка
        return res
