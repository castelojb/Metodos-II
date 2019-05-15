from unittest import TestCase
from Metodos.src.Modelo.Matematica.Funcoes.tangenteh import TangenteH
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha


class TestTangenteH(TestCase):
    def test_calcula(self):
        expressao = TangenteH(Folha())
        self.assertEqual(expressao.calcula(0), 0)
