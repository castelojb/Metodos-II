from Metodos.src.Modelo.Matematica.Funcoes.funcao import Funcao

"""
Conjunto de classes que realizam operacoes unarias nas funcoes
"""


class Potencia(Funcao):

    def __init__(self, expressao, expoente ):
        self.expressao = expressao
        self.expoente = expoente

    def __str__(self):
        return " ("+self.expressao.__str__()+")^"+self.expoente.__str__()+" "

    def __call__(self, valor):
        return pow(self.expressao(valor), self.expoente(valor))


class Raiz(Funcao):
    def __init__(self, expressao, expoente):
        self.expressao = expressao
        self.expoente = expoente

    def __str__(self):
        return " (" + self.expressao.__str__() + ")^1/" + self.expoente.__str__()+" "

    def __call__(self, valor):
        return pow(self.expressao(valor), 1/self.expoente(valor))
