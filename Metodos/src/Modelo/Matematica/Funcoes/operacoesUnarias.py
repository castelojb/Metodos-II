from funcao import Funcao

"""
Conjunto de classes que realizam operacoes unarias nas funcoes
"""


class Potencia(Funcao):

    def __init__(self, expressao, expoente ):
        self.expressao = expressao
        self.expoente = expoente

    def __str__(self):
        return " ("+self.expressao+")^"+self.expoente+" "

    def calcula(self, valor):
        return pow(self.expressao, self.expoente)


class Raiz(Funcao):
    def __init__(self, expressao, expoente):
        self.expressao = expressao
        self.expoente = expoente

    def __str__(self):
        return " (" + self.expressao + ")^1/" + self.expoente+" "

    def calcula(self, valor):
        return pow(self.expressao, 1/self.expoente)
