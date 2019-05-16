import numpy as np
from relatorio import RelatorioIntegral


def subdivideECalculadora(integral, funcao, erro, xi, xf):

    numeroDeParticoes = 1

    errop = 0

    while True:

        numeroDeParticoes = numeroDeParticoes *2

        etapas = []

        h = (xf - xi)/numeroDeParticoes

        for i in range(0, numeroDeParticoes):

            xip = xi + h*i
            xfp = xi + h*(i+1)

            etapas.append(integral.calcular(funcao, xip, xfp))

        if abs(np.sum(etapas) - errop) < abs(erro):
            break

        errop = np.sum(etapas)

    resp = RelatorioIntegral()

    resp.setResultado(np.sum(etapas))
    resp.setResultadosIndividuaisIntegral(etapas)

    return resp


