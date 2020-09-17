import random

def cross(populacao_codificada, selecionados, pelit):
    for _ in range(len(selecionados)):
        index_pai = random.randint(0, len(selecionados))
        index_mae = random.randint(0, len(selecionados))
        pai = populacao_codificada[index_pai]
        mae = populacao_codificada[index_mae]
        filho_um = pai[:int(len(pai)/2)] + mae[int(len(mae)/2):]
        filho_dois = mae[:int(len(mae)/2)] + pai[int(len(pai)/2):]
        
        populacao_codificada[index_pai] = filho_um
        populacao_codificada[index_mae] = filho_dois
    
    return populacao_codificada
