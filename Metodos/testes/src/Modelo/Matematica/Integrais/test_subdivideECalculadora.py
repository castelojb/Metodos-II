from unittest import TestCase
from Metodos.src.Modelo.Matematica.Integrais.Ferramentas import subdivideECalculadora
from Metodos.src.Modelo.Matematica.Integrais.metodosIntegracao import *
from Metodos.src.Modelo.Matematica.Funcoes.operacoesTrigonometricas import *
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha


class TestSubdivideECalculadora(TestCase):
    def test_subdivideECalculadora(self):

        print(subdivideECalculadora(GaussLegendre(3), Cosseno(Folha()), 0.001, 0, 1))

        print(subdivideECalculadora(NewtonCotes(4, filosofia=False), Cosseno(Folha()), 0.001, 0, 1))

