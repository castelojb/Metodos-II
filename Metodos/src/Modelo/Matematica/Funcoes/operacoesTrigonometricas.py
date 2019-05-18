from funcao import Funcao
from math import sin
from math import tanh
from math import cos

"""
Conunto de classes que realizam operacoes trigonometricas nas funcoes
"""


class Seno(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def __str__(self):
        return " sen("+self.subclass+") "

    def calcula(self, valor):
        return sin(self.subclass.calcula(valor))


class TangenteH(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def __str__(self):
        return " tanh(" + self.subclass + ") "

    def calcula(self, valor):
        return tanh(self.subclass.calcula(valor))


class Cosseno(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def __str__(self):
        return " cos(" + self.subclass + ") "

    def calcula(self, valor):
        return cos(self.subclass.calcula(valor))
