from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.cosseno import Cosseno
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha
from math import radians
from math import cos


class TestCosseno(TestCase):
    def test_calcula(self):
        expressao = Cosseno(Folha())

        self.assertEqual(expressao.calcula(radians(0)), cos(radians(0)))
        self.assertEqual(expressao.calcula(radians(90)), cos(radians(90)))
        self.assertEqual(expressao.calcula(radians(180)), cos(radians(180)))
        self.assertEqual(expressao.calcula(radians(270)), cos(radians(270)))
