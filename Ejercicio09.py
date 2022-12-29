def sumaRecursiva(a,b):
    if b == 0:
        respuesta = a
    else:
        respuesta =  sumaRecursiva(a,b-1)+1
    return respuesta

print(sumaRecursiva(10,15))

    