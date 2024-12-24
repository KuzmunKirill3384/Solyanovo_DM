from Natural import Natural
from Integer import Integer


class Rational:
    def __init__(self, num, denum):
        self.numerator = Integer(num)  # Числитель
        self.denumerator = Natural(denum)  # Знаменатель

    def __eq__(self, other):
        # Проверка на равенство
        if self.numerator.number.NZER_N_B() == False and other.numerator.number.NZER_N_B() == False:
            return True
        n1 = self.RED_Q_Q()  # Упрощение полного дроби
        n2 = other.RED_Q_Q()
        return n1.numerator == n2.numerator and n1.denumerator == n2.denumerator

    def __lt__(self, other):
        # Проверка на "меньше чем"
        n1 = self.RED_Q_Q()
        n2 = other.RED_Q_Q()
        t1 = n1.numerator.MUL_ZZ_Z(Integer(str(n2.denumerator)))
        t2 = n2.numerator.MUL_ZZ_Z(Integer(str(n1.denumerator)))
        return t1 < t2

    def __repr__(self):
        return self.__str__()  # Строковое представление

    def __gt__(self, other):
        # Проверка на "больше чем"
        n1 = self.RED_Q_Q()
        n2 = other.RED_Q_Q()
        t1 = n1.numerator.MUL_ZZ_Z(Integer(str(n2.denumerator)))
        t2 = n2.numerator.MUL_ZZ_Z(Integer(str(n1.denumerator)))
        return t1 > t2

    def __ne__(self, other):
        return not self.__eq__(other)  # Проверка на "не равно"

    def __str__(self):
        return f'{self.numerator}/{self.denumerator}'  # Формат дроби

    def RED_Q_Q(self):
        GCF = self.denumerator.GCF_NN_N(self.numerator.ABS_Z_N())  # Нахождение НОД
        gcf_result = Integer(str(GCF))
        RED = Rational(str(self.numerator.DIV_ZZ_Z(gcf_result)), str(self.denumerator.DIV_NN_N(GCF)))  # Упрощение
        return RED

    def INT_Q_B(self):
        # Проверка на целое число
        return self.RED_Q_Q().denumerator.COM_NN_D(Natural("1")) == 0

    @staticmethod
    def TRANS_Z_Q(num_z):
        # Преобразование целого числа в дробь
        numerator = Integer.copy(num_z)
        denumerator = Natural('1')
        num = numerator.MUL_ZZ_Z(Integer(str(num_z.ABS_Z_N())))
        result = Rational(str(num), str(denumerator))
        return result

    @staticmethod
    def copy(x):
        # Копирование объекта класса Rational
        res = Rational('', '')  # Новый пустой объект
        res.numerator = x.numerator  # Копируем числитель
        res.denumerator = x.denumerator  # Копируем знаменатель
        return res  # Возвращение копии

    def TRANS_Q_Z(self):
        # Преобразование дроби в целое число
        return Integer(str(self.RED_Q_Q().numerator))

    def ADD_QQ_Q(self, other):
        # Сложение дробей
        if self.numerator.number.NZER_N_B() == False:
            return other
        elif other.numerator.number.NZER_N_B() == False:
            return self
        Denum = self.denumerator.LCM_NN_N(other.denumerator)  # Общий знаменатель
        Num = self.numerator.MUL_ZZ_Z(Integer(str(Denum.DIV_NN_N(self.denumerator))))
        Num = Num.ADD_ZZ_Z(other.numerator.MUL_ZZ_Z(Integer(str(Denum.DIV_NN_N(other.denumerator)))))
        res = Rational(str(Num), str(Denum)).RED_Q_Q()  # Упрощение результата
        return res

    def SUB_QQ_Q(self, other):
        # Вычитание дробей
        if self.numerator.number.NZER_N_B() == False:
            return Rational(str(other.numerator.MUL_ZM_Z()), str(other.denumerator))  # Обратная дробь
        Opposite = Rational(str(other.numerator.MUL_ZM_Z()), str(other.denumerator))  # Смена знака
        SUB = self.ADD_QQ_Q(Opposite)  # Сложение с обратной
        return SUB

    def MUL_QQ_Q(self, other):
        # Умножение дробей
        if self.numerator.number.NZER_N_B() == False or other.numerator.number.NZER_N_B() == False:
            return Rational('0', '1')  # Умножение на ноль
        NUM = self.numerator.MUL_ZZ_Z(other.numerator)
        DENUM = self.denumerator.MUL_NN_N(other.denumerator)
        MUL = Rational(str(NUM), str(DENUM)).RED_Q_Q()  # Упрощение результата
        return MUL

    def DIV_QQ_Q(self, other):
        # Деление дробей
        NUM = Integer(str(other.denumerator))  # Числитель нового дроби
        DENUM = other.numerator.ABS_Z_N()  # Знаменатель нового дроби
        if other.numerator.POZ_Z_D() == 1:
            NUM = NUM.MUL_ZM_Z()  # Изменение знака если положительное
        DIV = self.MUL_QQ_Q(Rational(str(NUM), str(DENUM)))  # Умножение на обратную
        return DIV
