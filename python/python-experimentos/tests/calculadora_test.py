import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase, Calculadora):
    
    def test_restar_3menos2_devuelve1(self):
        calc=Calculadora()
        resultado=calc.restar(3,2)
        self.assertEqual(1, resultado)

    def test_edad_sinacio080994_debetener23anios(self):
        calc=Calculadora()
        resultado=calc.edad(8,9,1994)
        self.assertEqual(23, resultado)

