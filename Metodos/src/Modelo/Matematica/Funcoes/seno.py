from funcao import Funcao
from math import sin


class Seno(Funcao):

    def __init__(self, subclass):
        self.subclass = subclass

    def calcula(self, valor):
        return sin(self.subclass.calcula(valor))
