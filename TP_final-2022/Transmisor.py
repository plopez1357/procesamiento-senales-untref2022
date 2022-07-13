
def multiplexarSeñal(senales):
    señalMultiplexada = []
    cantidadCanales = len(senales)
    largoSeñal = len(senales[0])

    for i in range(largoSeñal):
        for j in range(cantidadCanales):
            señalMultiplexada.append(senales[j][i])
    
    return señalMultiplexada

'''
[1, 2, 3, 11]
[5, 6, 7, 12]
[8, 9, 0, 13]
[1, 5, 8, 2, 6, 9, 3, 7, 0, 11, 12, 13]
'''

