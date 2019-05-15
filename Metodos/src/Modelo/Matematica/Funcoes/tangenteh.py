from funcao import Funcao
from math import tanh


class TangenteH(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def calcula(self, valor):
        return tanh(self.subclass.calcula(valor))
