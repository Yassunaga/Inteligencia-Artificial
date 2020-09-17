def objetiva(individuo):
    numero_cromossomos = len(individuo)

    obj_function = 50
    for i in range(numero_cromossomos-1):
        obj_function -= individuo[i]**2

    return obj_function
