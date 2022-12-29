import random
def desordenar(lista, largolista , contador):
    if contador < largolista:
        NumeroRandom = random.randint(contador,largolista-1)
        lista[contador],lista[NumeroRandom] = lista[NumeroRandom],lista[contador]
        desordenar(lista,largolista,contador+1)
NumAleatorios =[1,2,3,4,5,6,7,8,9]
desordenar(NumAleatorios,len(NumAleatorios),0)
print(NumAleatorios)