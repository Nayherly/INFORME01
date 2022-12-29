def SeleccionOrden(lista,largoLista, contador):
    if contador < largoLista:
        pequeño = lista[contador]
        posicion = contador
        for i in range(contador+1,largoLista):
            if lista[i]<pequeño:
                pequeño = lista[i]
                posicion = i
        lista[contador], lista[posicion]=lista[posicion],lista[contador]
        seleccionOrden(lista,largoLista,contador+1)
A=[9,5,0,3,8,6,2,0,1]
SeleccionOrden(A,len(A),0)
print(A)