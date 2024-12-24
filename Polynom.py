from Natural import Natural
from Integer import Integer
from Rational import Rational

class Polynom:
    def __init__(self, parts: list):
        # Инициализация полинома
        self.degree = 0  # Степень полинома
        self.coefficients = []  # Список коэффициентов полинома
        try:
            self.degree = len(parts) - 1  # Установка степени полинома
            if self.degree < 0:
                raise ValueError  # Проверка на отрицательную степень полинома
            self.coefficients = [el for el in parts]  # Копирование коэффициентов
            # Конвертация коэффициентов типа Integer в Rational
            for i in range(len(self.coefficients)):
                if type(self.coefficients[i]) == Integer:
                    self.coefficients[i] = Rational(str(self.coefficients[i]), '1')
        except:
            self.degree = 0
            self.coefficients = []  # Пустой полином в случае исключения

    def __str__(self):
        # Преобразование полинома в строку для вывода
        s = []
        for i in range(self.degree + 1):
            s.append(str(self.coefficients[i]) + 'x^' + str(i))  # Формирует строку вида a_n*x^n + ... + a_0
        return ' + '.join(s[::-1])  # Обратный порядок для вывода

    @staticmethod
    def copy(x):
        # Создает копию полинома
        res = Polynom([])
        res.degree = x.degree
        for i in range(len(x.coefficients)):
            res.coefficients.append(x.coefficients[i])  # Копирование коэффициентов
        return res

    def ADD_PP_P(self, other):
        # Сложение двух полиномов
        res = Polynom([])
        if self.degree > other.degree:
            res.degree = self.degree
            for i in range(other.degree + 1):
                res.coefficients.append(self.coefficients[i].ADD_QQ_Q(other.coefficients[i]))  # Сложение коэффициентов
            # Добавление остальных коэффициентов
            for i in range(other.degree + 1, self.degree + 1):
                res.coefficients.append(Rational.copy(self.coefficients[i]))
        elif self.degree < other.degree:
            res.degree = other.degree
            for i in range(self.degree + 1):
                res.coefficients.append(self.coefficients[i].ADD_QQ_Q(other.coefficients[i]))  # Сложение коэффициентов
            # Добавление остальных коэффициентов
            for i in range(self.degree + 1, other.degree + 1):
                res.coefficients.append(Rational.copy(other.coefficients[i]))
        else:
            # Сложение полиномов одинаковой степени
            res.degree = self.degree
            for i in range(self.degree + 1):
                res.coefficients.append(self.coefficients[i].ADD_QQ_Q(other.coefficients[i]))
            # Удаление нулевых коэффициентов в конце
            while res.degree > 0 and res.coefficients[res.degree].INT_Q_B() and res.coefficients[
                res.degree].numerator.number.length == 1 and res.coefficients[res.degree].numerator.number.data[0] == 0:
                res.degree -= 1
                res.coefficients.pop()
        return res

    def SUB_PP_P(self, other):
        # Вычитание полиномов
        tmp = other.coefficients[:]  # Копирование коэффициентов
        res = Polynom(tmp)
        # Изменение знака коэффициентов другого полинома
        for i in range(len(other.coefficients)):
            res.coefficients[i] = Rational(str(res.coefficients[i].numerator.MUL_ZM_Z()),
                                           str(res.coefficients[i].denumerator))  # Умножение на -1
        return self.ADD_PP_P(res)  # Сложение текущего полинома и измененного

    def MUL_PQ_P(self, other):
        # Умножение полинома на рациональное число
        res = Polynom([])
        res.degree = self.degree
        for i in range(self.degree + 1):
            res.coefficients.append(self.coefficients[i].MUL_QQ_Q(other))  # Умножение каждого коэффициента на число
        return res

    def MUL_Pxk_P(self, k):
        # Умножение полинома на x^k
        res = Polynom([])
        res.degree = self.degree + k  # Новая степень полинома
        for i in range(k):
            res.coefficients.append(Rational("0", '1'))  # Добавление нулевых коэффициентов
        for i in range(self.degree + 1):
            res.coefficients.append(Rational.copy(self.coefficients[i]))  # Копирование оригинальных коэффициентов
        return res

    def LED_P_Q(self):
        # Возвращает ведущий коэффициент полинома (коэффициент при высшей степени)
        return Rational.copy(self.coefficients[self.degree])

    def DEG_P_N(self):
        # Возвращает степень полинома как целое число
        return Natural(str(self.degree))

    def FAC_P_Q(self):

        coef = self.coefficients[:]
        nums = [i.numerator.number for i in coef]  # Номера коэффициентов
        dens = [i.denumerator for i in coef]  # Знаменатели
        tmp_num = nums[0]  # Начинаем с первого числа
        for i in range(1, len(nums)):
            tmp_num = tmp_num.LCM_NN_N(nums[i])  # Нахождение НОК
        tmp_den = dens[0]
        for i in range(1, len(dens)):
            tmp_den = tmp_den.GCF_NN_N(dens[i])  # Нахождение НОД
        return Rational(str(tmp_num), str(tmp_den))  # Возвращаем нормализованный коэффициент

    def MUL_PP_P(self, other):
        # Умножение двух полиномов
        result = Polynom([])
        result.degree = self.degree + other.degree  # Новая степень
        for i in range(result.degree + 1):
            result.coefficients.append(Rational('0', '1'))  # Инициализация коэффициентов нулями
        for k in range(result.degree + 1):
            for i in range(k + 1):
                j = k - i
                # Проверка на допустимость индексов
                if (j <= other.degree) and (i <= self.degree):
                    tmp = self.coefficients[i].MUL_QQ_Q(other.coefficients[j])  # Умножение коэффициентов
                    result.coefficients[k] = result.coefficients[k].ADD_QQ_Q(tmp)  # Сложение результатов
        return result

    def DIV_PP_P(self, other):
        # Деление одного полинома на другой
        n = self.degree  # Степень делимого
        m = other.degree  # Степень делителя
        self_copy = Polynom(self.coefficients)  # Копия делимого
        if self.degree < other.degree:
            return 0  # Если степень делимого меньше степени делителя, результат 0
        result = Polynom([Rational('0', '1') for _ in range(n - m + 1)])  # Инициализация частного
        for i in range(n, m - 1, -1):
            result.coefficients[i - m] = self_copy.coefficients[i].DIV_QQ_Q(other.coefficients[m])  # Деление ведущих коэффициентов
            for j in range(m, -1, -1):
                self_copy.coefficients[i - m + j] = self_copy.coefficients[i - m + j].SUB_QQ_Q(
                    other.coefficients[j].MUL_QQ_Q(result.coefficients[i - m]))  # Вычитаем произведение
        return result  # Возвращает частное

    def MOD_PP_P(self, other):
        # Остаток от деления полиномов
        if self.degree < other.degree:
            return self  # Если степень делимого меньше степени делителя, остаток - это сам делимый
        coef = self.coefficients[:]  # Копирование коэффициентов
        result = Polynom(coef)  # Инициализация остатка
        return result.SUB_PP_P(other.MUL_PP_P(self.DIV_PP_P(other)))  # Остаток

    def GCF_PP_P(self, other):
        # Нахождение НОД двух полиномов
        def zip_longest_custom(*iterables, fillvalue=Rational('0', '1')):
            # Создание итераторов одной длины, заполняя недостающие элементы
            max_length = max(len(iterable) for iterable in iterables)
            for i in range(max_length):
                yield tuple(iterable[i] if i < len(iterable) else fillvalue for iterable in iterables)

        def compare_polynomials(poly1, poly2):
            # Сравнение двух полиномов
            if len(poly1) > len(poly2):
                return 1
            if len(poly1) < len(poly2):
                return -1
            for elem1, elem2 in list(zip_longest_custom(poly1, poly2)):
                if elem1 > elem2:
                    return 1
                elif elem1 == elem2:
                    continue
                else:
                    return -1
            return 0

        p1 = Polynom(self.coefficients)  # Копия первого полинома
        p2 = Polynom(other.coefficients)  # Копия второго полинома
        while compare_polynomials(p1.coefficients, [Rational('0', '1')]) and compare_polynomials(p2.coefficients,
                                                                                                 [Rational('0', '1')]):
            # В цикле находим НОД пока оба полинома не равны 0
            if p1.degree == p2.degree and compare_polynomials(p1.coefficients, p2.coefficients) == -1:
                for i in range(p1.degree + 1):
                    p1.coefficients[i] = p1.coefficients[i].MUL_QQ_Q(p2.coefficients[-1])  # Умножаем на старший коэффициент второго полинома
            if compare_polynomials(p1.coefficients, p2.coefficients) == 1:  # Если p1 > p2
                p1, p2 = p2, p1.MOD_PP_P(p2)  # Меняем местами и находим остаток
            elif compare_polynomials(p1.coefficients, p2.coefficients) == 1:  # Если p1 < p2
                return p1
        for i in range(len(p1.coefficients)):
            p1.coefficients[i] = p1.coefficients[i].DIV_QQ_Q(p1.coefficients[-1])  # Нормализация результата
        return p1  # Возвращает НОД

    def DER_P_P(self):
        # Производная полинома
        result = []
        for i in range(1, len(self.coefficients)):
            c = self.coefficients[i].MUL_QQ_Q(Rational(str(i), '1'))  # Умножаем коэффициент i на x^(i-1)
            result.append(c)
        result = Polynom(result)  # Возвращает новый полином как производную
        return result

    def NMR_P_P(self):
        # Нахождение нормированной производной
        g = self.GCF_PP_P(self.DER_P_P())  # Находим НОД и производную
        result = self.DIV_PP_P(g)  # Делим исходный полином на этот НОД
        return result  # Возвращает нормированную производную


'''# Создание полинома x^100 + 1
coeffs_1 = [Rational('1', '1')] + [Rational('0', '1')] * 99 + [Rational('1', '1')]
p1 = Polynom(coeffs_1)  # Это полином x^100 + 1

# Создание полинома x + 1
coeffs_2 = [Rational('1', '1'), Rational('1', '1')]
p2 = Polynom(coeffs_2)  # Это полином x + 1
print(f"Полином P1: {p1}")
print(f"Полином P2: {p2}")

quotient = p1.DIV_PP_P(p2)
print(f"Частное от деления P1 на P2: {quotient}")'''