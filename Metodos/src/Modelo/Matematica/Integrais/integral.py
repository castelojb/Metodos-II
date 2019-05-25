import abc

"""
Interface para implementar integrais
"""


class Integral(abc.ABC):
    """
    Metodo para calculo da integral
    @:param f: Funcao em que sera aplicada a integral
    @:param xi: X inicial
    @:param xf: X final
    @:return: Um numero que eh o valor da integral
    """
    @abc.abstractmethod
    def __call__(self, f, xi, xf):
        pass
