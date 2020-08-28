import numpy
from random import random

num_individuos = 100
num_cromossomos = 3
limites_cromossomos = numpy.matrix('0 5; 0 30; 0 1000')

def gerar_populacao(numero_individuos, limites_cromossomos):
    num_cromossomos = len(limites_cromossomos)

    populacao = []
    for i in range(0, numero_individuos):
        individuo = []
        for j in range(0, num_cromossomos):
            inf = limites_cromossomos[j, 0]
            sup = limites_cromossomos[j, 1]
            individuo.append(round(random() * (sup - inf) + inf)) 
        populacao.append(individuo)

    return populacao

def main():
    populacao = gerar_populacao(num_individuos, limites_cromossomos)
    print(populacao)

if __name__ == "__main__":
    main()
