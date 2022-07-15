def multiplexarSeñal(senales):
    señalMultiplexada = []
    cantidadCanales = len(senales)
    largoSeñal = len(senales[0])
    for i in range(largoSeñal):
        for j in range(cantidadCanales):
            señalMultiplexada.append(senales[j][i])
    return señalMultiplexada

