import numpy
from random import random

num_individuos = 100
num_cromossomos = 3
limites_cromossomos = numpy.matrix('0 5; 0 30; 0 255')

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

def codificacao(populacao, limite_cromossomos):
    num_individuos = len(populacao)
    num_cromossomos = len(limite_cromossomos)

    populacao_codificada = []
    for i in range(0, num_individuos):
        temp = []
        for j in range(0, num_cromossomos):
            temp.append(bin(populacao[i][j]))
        populacao_codificada.append(temp)
    return populacao_codificada


def decodificacao(populacao_codificada, limites_cromossomos):
    num_individuos = len(populacao_codificada)
    num_cromossomos = len(limites_cromossomos)

    populacao_decodificada = []
    for i in range (0, num_individuos):
        individuo = populacao_codificada[i]
        temp = []
        for j in range(0, num_cromossomos):
            temp.append(int(individuo[j], 2))
        populacao_decodificada.append(temp)
    
    return populacao_decodificada

def main():
    populacao = gerar_populacao(num_individuos, limites_cromossomos)
    print(f"Populacao Gerada: \n{populacao}", end="\n\n")
    populacao_codificada = codificacao(populacao, limites_cromossomos)
    print(f"Populacao Codificada: \n{populacao_codificada}", end="\n\n")
    populacao_decodificada = decodificacao(populacao_codificada, limites_cromossomos)
    print(f"Populacao Decodificada: \n{populacao_decodificada}", end="\n\n")

if __name__ == "__main__":
    main()