from Metodos.src.Modelo.Matematica.Algebra.matriz import Matriz
import numpy as np


def GerarIdentidade(dimensao):
    resposta = Matriz(dimensao, dimensao)

    for i in range(dimensao):
        resposta[i, i]= 1

    return resposta


def GerarLowerUpper(A):

    lower = GerarIdentidade(A.getColunas())
    upper = A.clone()

    for i in range(A.getColunas()):

        for j in range(A.getColunas()):

            for k in range(i):

                upper[i, j] = upper[i, j] - (lower[i, k] * upper[k, j])

        for m in range(A.getLinhas()):
            lower[m, i] = A[m, i]

            for k in range(i):
                lower[m, i] = A[m, i] - (lower[m, k] * upper[k, i])

            lower[m, i] = lower[m, i] / upper[i, i]

    return lower, upper


def GerarMatrizEliminacaoGauss(matrizProblema, vetorColuna, comZeros = True):

    A = matrizProblema.copy()
    b = vetorColuna.copy()

    for k in range(A.getLinhas()-1):

        for i in range(A.getLinhas()):

            m = -A[i, k] / A[k, k]

            for j in range(A.getLinhas()):

                A[i, j] = A[i, j] + (m * A[k, j])

            b[i, 0] = b[i, 0] + (m * b[k, 0])

    if comZeros:

        for i in range(A.getLinhas()):

            for j in range(A.getColunas()):

                if j<i:
                    A[i, j] = 0

    return A, b


def ResolverSistema(A, b, triangular_superior = True):

    resposta = Matriz(b.getLinhas(), 1)

    n = A.getLinhas() - 1

    if triangular_superior:

        resposta[n, 0] = b[n, 0] / A[n, n]

        for i in range(n, -1, -1):

            soma = 0

            for j in range(i+1, n+1, 1):

                soma += A[i, j] * resposta[j, 0]

            resposta[i, 0] = (b[i, 0]-soma)/A[i, i]
    else:

        for i in range(0, n+1, 1):

            soma = 0

            for j in range(i):

                soma += A[i, j] * resposta[j, 0]

            resposta[i, 0] = (b[i, 0]-soma)/A[i, i]

    return resposta


def GerarMatrizInversa(A):

    L, U = GerarLowerUpper(A)

    I = GerarIdentidade(A.getColunas())

    m_inversa = []

    for i in range(A.getColunas()):

        xi = ResolverSistema(L, I.getValoresColuna(i), triangular_superior=False)

        coluna_inversa = ResolverSistema(U, xi)

        m_inversa.append(coluna_inversa)

    resposta = Matriz(A.getLinhas(), A.getColunas())

    resposta.matriz = np.matrix(m_inversa)

    return resposta


def LeitorDeArquivo(caminho, sep=" "):

    with open(caminho, 'r') as file:

        matriz = []

        for line in file:

            matriz.append((line.split(sep)))

    matrizArray = np.matrix(matriz)

    resposta = Matriz(matrizArray.shape[0], matrizArray.shape[1])

    resposta.matriz = matrizArray

    return resposta
