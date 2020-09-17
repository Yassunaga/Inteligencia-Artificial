from funcao_objetivo import objetiva


def fitness(populacao):
    num_individuos = len(populacao)
    num_cromossomos = len(populacao[0])
    
    fitness = []
    for i in range(num_individuos):
        fitness.append(objetiva(populacao[i]))
    
    return fitness
