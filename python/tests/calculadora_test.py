import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase, Calculadora):
    def test_restar_3menos2_devuelve1(self):
        calc=Calculadora()
        resultado=calc.restar(3,2)
        self.assertEqual(1, resultado)

    def test_edad_sinacio24041998_debeTener20anios(self):
        calc=Calculadora()
        resultado=calc.edad(24,4,1998)
        self.assertEqual(20, resultado)

        


