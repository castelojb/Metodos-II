from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.polinomio import Polinomio
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha


class TestPolinomio(TestCase):
    def test_calcula(self):
        expressao = Polinomio(Folha())
        self.assertEqual(expressao.calcula(0), 5)
        self.assertEqual(expressao.calcula(1), 9)
