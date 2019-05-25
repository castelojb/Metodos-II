import numpy as np
import numpy.matlib


class Matriz:

    def __init__(self, numeroLinhas, numeroColunas):
        self.numeroLinhas = numeroLinhas
        self.numeroColunas = numeroColunas
        self.matriz = np.matlib.zeros((numeroLinhas, numeroColunas))

    def getColunas(self):
        return self.numeroColunas

    def getLinhas(self):
        return self.numeroLinhas

    def __getitem__(self, posicao):
        return self.matriz[posicao]

    def __setitem__(self, key, valor):
        self.matriz[key] = valor

    def __str__(self):
        return str(self.matriz)

    def transposta(self):
        matrizTransposta = np.transpose(self.matriz)
        resposta = Matriz(matrizTransposta.shape[0], matrizTransposta.shape[1])
        resposta.matriz = matrizTransposta
        return resposta

    def __add__(self, valor):
        matrizAlterada = self.matriz + valor.matriz
        resposta = Matriz(matrizAlterada.shape[0], matrizAlterada.shape[1])
        resposta.matriz = matrizAlterada
        return resposta

    def __sub__(self, valor):
        matrizAlterada = self.matriz - valor.matriz
        resposta = Matriz(matrizAlterada.shape[0], matrizAlterada.shape[1])
        resposta.matriz = matrizAlterada
        return resposta

    def __mul__(self, valor):
        if isinstance(valor, Matriz):
            matrizAlterada = self.matriz * valor.matriz
            resposta = Matriz(matrizAlterada.shape[0], matrizAlterada.shape[1])
            resposta.matriz = matrizAlterada
        else:
            matrizAlterada = self.matriz * valor
            resposta = Matriz(matrizAlterada.shape[0], matrizAlterada.shape[1])
            resposta.matriz = matrizAlterada

        return resposta

    def __truediv__(self, valor):
        matrizAlterada = self.matriz / valor
        resposta = Matriz(matrizAlterada.shape[0], matrizAlterada.shape[1])
        resposta.matriz = matrizAlterada
        return resposta

    def __matmul__(self, valor):
        dimensaoCompativel = self.matriz.shape == valor.matriz.shape or self.matriz.shape == valor.transposta().matriz.shape

        saoVetores = (self.matriz.shape[0] == 1 or self.matriz.shape[1] == 1) and (
                    valor.matriz.shape[0] == 1 or valor.matriz.shape[1] == 1)

        if dimensaoCompativel and saoVetores:

            soma = 0
            for elemento1, elemento2 in zip(self.matriz, valor.matriz):
                print(elemento1, elemento2)
                soma += elemento1 * elemento2
            return soma[0, 0]
        else:
            print("dimensao {} nao eh compativel com {}".format(self.matriz.shape, valor.matriz.shape))
            raise

    def norma(self):
        if (self.matriz.shape[0] == 1 or self.matriz.shape[1] == 1):
            return np.linalg.norm(self.matriz)
        else:
            print("dimensao {} nao eh compativel com vetor".format(self.matriz.shape))
            raise

    def __eq__(self, valor):
        return (self.matriz == valor.matriz).all()

    def getValoresColuna(self, coluna):
        mcol = self.matriz[:, coluna]
        resposta = Matriz(mcol.shape[0], mcol.shape[1])
        resposta.matriz = mcol
        return resposta

    def getValoresLinha(self, linha):
        mlin = self.matriz[linha, :]
        resposta = Matriz(mlin.shape[0], mlin.shape[1])
        resposta.matriz = mlin
        return resposta

    def copy(self):
        mcopia = self.matriz.copy()
        resposta = Matriz(mcopia.shape[0], mcopia.shape[1])
        resposta.matriz = mcopia
        return resposta