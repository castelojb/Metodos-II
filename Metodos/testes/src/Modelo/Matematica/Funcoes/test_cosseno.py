from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.cosseno import Cosseno
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha
from math import pi


class TestCosseno(TestCase):
    def test_calcula(self):
        expressao = Cosseno(Folha())

        self.assertEqual(expressao.calcula(0), 1)
        self.assertEqual(expressao.calcula(pi/2).__round__(), 0)
