from random import randint


def selecao_roleta(lista_aptidoes: list, quantos_selecionar: int):
    probabilidades = []
    inicio = 0
    for aptidao in lista_aptidoes:
        intervalo = {
            "inicio": inicio,
            "fim": inicio + aptidao
        }
        inicio = inicio + aptidao + 1
        probabilidades.append(intervalo)
    
    minimo = probabilidades[0]['inicio']
    maximo = probabilidades[len(lista_aptidoes) - 1]['fim']

    valores_selecionados = []
    for i in range(quantos_selecionar):
        valores_selecionados.append(randint(minimo, maximo))

    indices_selecionados = []
    for valor in valores_selecionados:
        for index, probabilidade in enumerate(probabilidades):
            if valor >= probabilidade['inicio'] and valor < probabilidade['fim']:
                indices_selecionados.append(index)
    
    return indices_selecionados
