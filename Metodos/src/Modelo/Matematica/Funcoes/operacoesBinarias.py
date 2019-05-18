from funcao import Funcao

"""
Conjunto de classes que realizam operacoes binarias sobre as expressoes
"""


class Soma(Funcao):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def __str__(self):
        return " ("+self.exp1+" + "+self.exp2+") "

    def calcula(self, valor):
        return self.exp1.calcula(valor) + self.exp2.calcula(valor)


class Subtracao(Funcao):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def __str__(self):
        return " ("+self.exp1+" - "+self.exp2+") "

    def calcula(self, valor):
        return self.exp1.calcula(valor) - self.exp2.calcula(valor)


class Multiplicacao(Funcao):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def __str__(self):
        return " ("+self.exp1+" * "+self.exp2+") "

    def calcula(self, valor):
        return self.exp1.calcula(valor) * self.exp2.calcula(valor)


class Divisao(Funcao):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def __str__(self):
        return " ("+self.exp1+" / "+self.exp2+") "

    def calcula(self, valor):
        return self.exp1.calcula(valor) / self.exp2.calcula(valor)


