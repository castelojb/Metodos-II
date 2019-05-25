from Metodos.src.Modelo.Matematica.Algebra.utils.ferramentasMatriz import GerarMatrizInversa


def Potenciacao(A, x0, erro):

    q = x0 / x0.norma()

    x = A * q

    lamb = (q.transposta() * x)[0, 0]

    while True:

        lamb0 = lamb

        q = x / x.norma()

        x = A * q

        lamb = (q.transposta() * x)[0, 0] / (q.transposta() * q)[0, 0]

        if (lamb - lamb0)/lamb < erro:
            break

    return lamb, x


def PotenciacaoReversa(A, x0, erro):
    return Potenciacao(GerarMatrizInversa(A), x0, erro)
