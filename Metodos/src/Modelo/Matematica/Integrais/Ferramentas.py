from numpy import sum
from relatorio import RelatorioIntegral

"""
Conjunto de funcoes que vao auxiliar no calculo de uma integral
"""

"""
Funcao que particiona a integral e vai claculando seu valor ate satizfazer o erro ou atingir o numero de iteracoes maximo
@:param integral: o objeto integral que sera aplicado
@:param funcao: a funcao que sera aplicada
@:param erro: o criterio se parada que sera avaliado
@:param xi: X inicial
@:param xf: X final
@:param itMax: numero maximo de iteracoes
@:return: uma classe de Realatorio
"""


def subdivideECalculadora(integral, funcao, erro, xi, xf, itMax=300):

    numeroDeParticoes = 1
    integralAnterior = 0
    iteracoes = 0

    numeroDeParticoesRelatorio = []
    integralAnteriorRelatorio = []
    integralAtualRelatorio = []
    erroRelatorio = []
    continuaRelatorio = []

    while True:

        integralAtual = []

        h = (xf - xi)/numeroDeParticoes

        for i in range(0, numeroDeParticoes):

            xip = xi + h*i
            xfp = xi + h*(i+1)

            integralAtual.append(integral(funcao, xip, xfp))

        resultadoIntegralAtual = sum(integralAtual)
        erroAtual = abs(resultadoIntegralAtual - integralAnterior)

        numeroDeParticoesRelatorio.append(numeroDeParticoes)
        integralAnteriorRelatorio.append(integralAnterior)
        integralAtualRelatorio.append(resultadoIntegralAtual)
        erroRelatorio.append(erroAtual)

        if erroAtual < abs(erro) or (iteracoes == itMax):
            resultado = resultadoIntegralAtual
            continuaRelatorio.append(False)
            break

        integralAnterior = resultadoIntegralAtual
        numeroDeParticoes = numeroDeParticoes * 2
        continuaRelatorio.append(True)
        iteracoes += 1

    retorno = RelatorioIntegral(resultado,
                                numeroDeParticoesRelatorio,
                                integralAnteriorRelatorio,
                                integralAtualRelatorio,
                                erroRelatorio,
                                continuaRelatorio)
    return retorno


