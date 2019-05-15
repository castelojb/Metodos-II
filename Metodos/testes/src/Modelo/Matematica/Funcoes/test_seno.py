from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.seno import Seno
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha


class TestSeno(TestCase):
    def test_calcula(self):
        expressao = Seno(Folha())
        self.assertEqual(expressao.calcula(0), 0)
