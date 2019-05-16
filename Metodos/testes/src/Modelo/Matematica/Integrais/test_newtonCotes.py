from unittest import TestCase
from Metodos.src.Modelo.Matematica.Integrais.newtoncotes import NewtonCotes


class TestNewtonCotes(TestCase):
    def test_calcula(self):
        print(isinstance(NewtonCotes(), NewtonCotes))
        self.fail()
