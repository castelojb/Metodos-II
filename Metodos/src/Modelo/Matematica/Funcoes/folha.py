from funcao import Funcao

"""
Classe especial que representa a variavel 'x'
"""


class Folha(Funcao):
    def __str__(self):
        return "x"

    def __call__(self, valor):
        return valor
