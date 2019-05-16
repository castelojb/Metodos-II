from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.tangenteh import TangenteH
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha
from math import tanh
from math import radians


class TestTangenteH(TestCase):
    def test_calcula(self):
        expressao = TangenteH(Folha())

        self.assertEqual(expressao.calcula(radians(0)), tanh(radians(0)))
        self.assertEqual(expressao.calcula(radians(30)), tanh(radians(30)))
        self.assertEqual(expressao.calcula(radians(90)), tanh(radians(90)))
        self.assertEqual(expressao.calcula(radians(180)), tanh(radians(180)))
        self.assertEqual(expressao.calcula(radians(270)), tanh(radians(270)))
