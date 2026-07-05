import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(3, 5), 8)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

if __name__ == "__main__":
    unittest.main()

