from unittest import TestCase
from Metodos.src.Modelo.Matematica.Integrais.Ferramentas import subdivideECalculadora
from Metodos.src.Modelo.Matematica.Integrais.newtoncotes import NewtonCotes
from Metodos.src.Modelo.Matematica.Integrais.gausslegendre import GaussLegendre
from Metodos.src.Modelo.Matematica.Funcoes.seno import Seno
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha
from Metodos.src.Modelo.Matematica.Funcoes.cosseno import Cosseno
from Metodos.src.Modelo.Matematica.Funcoes.polinomio import Polinomio


class TestSubdivideECalculadora(TestCase):
    def test_subdivideECalculadora(self):

        print(GaussLegendre(1).calcular((Folha()), 0, 1))

        print(subdivideECalculadora(GaussLegendre(2), Cosseno(Folha()), 0.001, 0, 1).getResultado())

        print(subdivideECalculadora(NewtonCotes(4, filosofia=False), Cosseno(Folha()), 0.001, 0, 1).getResultado())
        #self.fail()
