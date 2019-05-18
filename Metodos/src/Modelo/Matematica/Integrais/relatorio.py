import pandas as pd


"""
Classe auxiliar para gerar um relatorio do calculo sequencial de uma integral
"""


class RelatorioIntegral:

    def __init__(self, resultado, numeroDeParticoes, integralAnterior, integralAtual, erro, continua):
        self.resultado = resultado
        self.numeroDeParticoes = numeroDeParticoes
        self.integralAnterior = integralAnterior
        self.integralAtual = integralAtual
        self.erro = erro
        self.continua = continua

        obj = {"nPart": self.numeroDeParticoes,
               "Iant": self.integralAnterior,
               "Iatual": self.integralAtual,
               "Erro": self.erro,
               "Continua": self.continua}

        self.dataFrame = pd.DataFrame(data=obj)

    def __str__(self):
        return self.dataFrame.__str__()

    def getDataFrame(self):
        return self.dataFrame



