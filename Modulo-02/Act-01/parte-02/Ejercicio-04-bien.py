def buscar_elemento(arreglo, elemento):

    for i, num in enumerate(arreglo):
        if num == elemento:
            return i
    return "El elemento no se encuentra en el arreglo."

numeros = [7, 12, 34, 43, 78]

elemento_a_buscar = 43
posicion = buscar_elemento(numeros, elemento_a_buscar)

print(f"El valor {elemento_a_buscar} se encuentra en la posición {posicion}.")