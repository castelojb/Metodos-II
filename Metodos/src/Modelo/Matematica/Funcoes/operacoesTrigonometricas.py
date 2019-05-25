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

    def __call__(self, valor):
        return sin(self.subclass(valor))


class TangenteH(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def __str__(self):
        return " tanh(" + self.subclass + ") "

    def __call__(self, valor):
        return tanh(self.subclass(valor))


class Cosseno(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def __str__(self):
        return " cos(" + self.subclass + ") "

    def __call__(self, valor):
        return cos(self.subclass(valor))
