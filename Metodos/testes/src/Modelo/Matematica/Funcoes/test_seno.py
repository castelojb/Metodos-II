from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.seno import Seno
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha
from math import radians
from math import sin


class TestSeno(TestCase):
    def test_calcula(self):
        expressao = Seno(Folha())

        self.assertEqual(expressao.calcula(radians(0)), sin(radians(0)))
        self.assertEqual(expressao.calcula(radians(90)), sin(radians(90)))
        self.assertEqual(expressao.calcula(radians(180)), sin(radians(180)))
        self.assertEqual(expressao.calcula(radians(270)), sin(radians(270)))
