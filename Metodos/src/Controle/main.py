from Metodos.src.Modelo.Matematica.Funcoes.constante import Constante
from Metodos.src.Modelo.Matematica.Funcoes.folha import Folha
from Metodos.src.Modelo.Matematica.Funcoes.operacoesBinarias import *
from Metodos.src.Modelo.Matematica.Funcoes.operacoesTrigonometricas import *
from Metodos.src.Modelo.Matematica.Funcoes.operacoesUnarias import *

f = Divisao(Folha(),
           Constante(2))

print(f(1))
print(f(2))
print(f(3))
print(Folha())
print(Divisao(Folha(),
        2))
print(f)

f= Soma(Seno( Multiplicacao(Constante(2),Potencia(Folha(),Constante(2))) ),
       Cosseno(Divisao(Constante(1),Folha())))
print(f(1))


