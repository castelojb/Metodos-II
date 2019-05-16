import numpy as np


class RelatorioIntegral:

    def __init__(self):
        self.__resultado = 0
        self.__resultadosIndividuaisIntegral = []

    def setResultado(self, valor):
        self.__resultado = valor

    def getResultado(self):
        return self.__resultado

    def appendEtapa(self, valor):
        self.__resultadosIndividuaisIntegral.append(valor)

    def getResultadosIndividuaisIntegral(self):
        return self.__resultadosIndividuaisIntegral

    def setResultadosIndividuaisIntegral(self, resultadosArray):
        self.__resultadosIndividuaisIntegral = resultadosArray



