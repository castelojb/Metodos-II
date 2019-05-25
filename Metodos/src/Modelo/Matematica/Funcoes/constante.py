from funcao import Funcao

"""
Classe especial que representa uma constante
"""


class Constante(Funcao):

    def __init__(self, k):
        self.__constante = k

    def __str__(self):
        return str(self.__constante)

    def __call__(self, valor):
        return self.__constante
