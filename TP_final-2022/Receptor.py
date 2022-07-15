def demultiplexarSeñal(señalMultiplexada, cantCanales):
    señalesDemultiplexadas = []
    for i in range(cantCanales):
        señalesDemultiplexadas.append(señalMultiplexada[i::cantCanales])
    return señalesDemultiplexadas