from math import sqrt
from integral import Integral

"""
Conjunto de Metodos para calculo de Integrais
"""


class GaussLegendre(Integral):
    def __init__(self, grau=1):
        self.__grau = grau

    def setGrau(self, valor):
        self.__grau = valor

    def calcular(self, f, xi, xf):

        if self.__grau == 1:

            return ((xf-xi)/2) * 2*f.calcula(0)

        elif self.__grau == 2:

            print((f.calcula(1/sqrt(3)) + f.calcula(-1/sqrt(3))))

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


class NewtonCotes(Integral):

    def __init__(self, grau=1, filosofia=True):
        self.__grau = grau
        self.__filosofia = filosofia

    def setFilosofia(self, filosofia):
        self.__filosofia=filosofia

    def setGrau(self, grau):
        self.__grau = grau

    def calcular(self, f, xi, xf):

        if self.__filosofia:
            if self.__grau == 1:

                h = xf - xi

                return (h/2)*(f.calcula(xi) + f.calcula(xf))

            elif self.__grau == 2:

                h = (xf - xi) / 2

                return (h/3) * (f.calcula(xi) + 4*f.calcula(xi+h) + f.calcula(xf))

            elif self.__grau == 3:

                h = (xf-xi)/3

                return ((3*h)/8) * (f.calcula(xi) + 3*f.calcula(xi+h) + 3*f.calcula(xi+2*h) + f.calcula(xf))

            elif self.__grau == 4:

                h = (xf-xi)/4

                return (h/90) * (7*f.calcula(xi) + 32*f.calcula(xi+h) + 12*f.calcula(xi+2*h) + 32*f.calcula(xi+3*h) + 7*f.calcula(xf))

            else:
                raise ValueError('grau invalido')

        else:

            if self.__grau == 0:

                h = (xf-xi)/2

                return 2*h*(f.calcula(xi+h))

            elif self.__grau == 1:

                h = (xf-xi)/3

                return ((3*h)/2) * (f.calcula(xi+h) + f.calcula(xi + 2*h))

            elif self.__grau == 2:

                h = (xf-xi)/4

                return ((4*h)/3) * (2*f.calcula(xi+h) - f.calcula(xi+2*h) + 2*f.calcula(xi+3*h))

            elif self.__grau == 3:

                h = (xf-xi)/5

                return ((5*h)/24) * (11*f.calcula(xi+h) + f.calcula(xi+2*h) + f.calcula(xi+3*h) + 11*f.calcula(xi+4*h))

            elif self.__grau == 4:

                h = (xf-xi)/6

                return ((3*h)/10) * (11*f.calcula(xi+h) - 14*f.calcula(xi+2*h) + 26*f.calcula(xi+3*h) - 14*f.calcula(xi+4*h) + 11*f.calcula(xi+5*h))

            else:
                raise ValueError('grau invalido')
