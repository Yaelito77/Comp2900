def encontrar_indice(lista, elemento):
    for n, valor in enumerate(lista):
        if valor == elemento:
            return n
    return -1

lista = [5, 4, 3, 2, 1]
elemento_buscar = 1
indice = encontrar_indice(lista, elemento_buscar)
if indice != -1:
    print(f"El elemento {elemento_buscar} se encuentra en el indice {indice} de la lista.")
else:
    print(f"El elemento {elemento_buscar} no se encuentra en la lista.")