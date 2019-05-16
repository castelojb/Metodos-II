import abc


class Integral(abc.ABC):

    @abc.abstractmethod
    def calcular(self, f, xi, xf):
        pass
