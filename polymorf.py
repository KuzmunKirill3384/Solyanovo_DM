import unittest
from Polynom import Polynom
from Integer import Integer
from Rational import Rational

class TestPolynom(unittest.TestCase):

    def setUp(self):
        # Установка полиномов для использования в тестах
        self.p1 = Polynom([Rational('1', '1'), Rational('0', '1'), Rational('3', '1')])  # 3x^2 + 0x + 1
        self.p2 = Polynom([Rational(2, 1), Rational(1, 1)])  # 1x + 2
        self.p3 = Polynom([Rational(0, 1)])  # Нулевой полином
        self.p4 = Polynom([])  # Пустой полином

    def test_addition(self):
        result = self.p1.ADD_PP_P(self.p2)
        expected = Polynom([Rational(1, 1), Rational(1, 1), Rational(3, 1)])  # 3x^2 + 1x + 3
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_subtraction(self):
        result = self.p1.SUB_PP_P(self.p2)
        expected = Polynom([Rational(-2, 1), Rational(-1, 1), Rational(3, 1)])  # 3x^2 - 1x - 2
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_multiplication(self):
        result = self.p1.MUL_PP_P(self.p2)
        # Ожидаем 2x^3 + 1x^2 + 6x + 3 (2*3=6, 2,1,0)
        expected = Polynom([Rational(3, 1), Rational(6, 1), Rational(1, 1), Rational(2, 1)])
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_division(self):
        result = self.p1.DIV_PP_P(self.p2)  # 3x^2 + 1 / x + 2
        expected = Polynom([Rational(3, 1)])  # Ожидаем 3x^1 (это только старший коэффициент, остальное игнорируем)
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_derivative(self):
        result = self.p1.DER_P_P()  # Производная
        expected = Polynom([Rational(6, 1), Rational(0, 1)])  # 6x + 0
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_normalized_derivative(self):
        result = self.p1.NMR_P_P()  # Нормализованная производная
        expected = Polynom([Rational(6, 1)])  # Убрать всем нули
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_zero_polynomial(self):
        result = self.p3.ADD_PP_P(self.p1)
        expected = self.p1  # Нулевой полином + Полином = Полином
        self.assertEqual(result.coefficients, expected.coefficients)

    def test_empty_polynomial(self):
        result = self.p4.ADD_PP_P(self.p1)
        expected = self.p1  # Пустой полином + Полином = Полином
        self.assertEqual(result.coefficients, expected.coefficients)

if __name__ == '__main__':
    unittest.main()