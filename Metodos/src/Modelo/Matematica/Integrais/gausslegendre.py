from math import sqrt
from integral import Integral


class GaussLegendre(Integral):
    def __init__(self, grau=1):
        self.__grau = grau

    def setGrau(self, valor):
        self.__grau = valor

    def calcular(self, f, xi, xf):

        if self.__grau == 1:

            return ((xf-xi)/2) * 2*f.calcula(0)

        elif self.__grau == 2:

            print(((xf-xi)/2) * (f.calcula(1/sqrt(3)) + f.calcula(-1/sqrt(3))))

            return ((xf-xi)/2) * (f.calcula(1/sqrt(3)) + f.calcula(-1/sqrt(3)))

        elif self.__grau == 3:

            return ((xf-xi)/2) * ((5/9)*f.calcula(-sqrt(3/5)) + (8/9)*f.calcula(0) + (5/9)*f.calcula(sqrt(3/5)))

        elif self.__grau == 4:

            term1 = ((18+sqrt(30))/36) * f.calcula(-sqrt((3/7) - ((2*sqrt(30))/35)))
            term2 = ((18+sqrt(30))/36) * f.calcula(sqrt((3/7) - ((2*sqrt(30))/35)))
            term3 = ((18-sqrt(30))/36) * f.calcula(-sqrt((3/7) + ((2*sqrt(30))/35)))
            term4 = ((18-sqrt(30))/36) * f.calcula(sqrt((3/7) + ((2*sqrt(30))/35)))

            return ((xf-xi)/2) * (term1+term2+term3+term4)

        else:
            raise ValueError('grau invalido')
