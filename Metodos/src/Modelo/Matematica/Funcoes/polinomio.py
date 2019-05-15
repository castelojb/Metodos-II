from funcao import Funcao


class Polinomio(Funcao):

    def __init__(self,expressao):
        self.expressao = expressao

    def calcula(self, valor):
        return 4*self.expressao.calcula(valor)**2 + 5
