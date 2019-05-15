from funcao import Funcao
from math import cos


class Cosseno(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def calcula(self, valor):
        return cos(self.subclass.calcula(valor))
