import abc


'''
Interface formal para implementar funcoes matematicas
'''
class Funcao(abc.ABC):
    '''
    Metodo para retornar calcular o valor de uma funcao
    @:param valor: valor 'x' da funcao
    @:return o valor da funcao implementada
    '''
    @abc.abstractmethod
    def calcula(self, valor):
        pass