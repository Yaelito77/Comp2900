def busqueda_binaria(lista, posicion):
    
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == posicion:
            return medio
        elif lista[medio] < posicion:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

miLista = [3, 7, 10, 14, 19, 26, 35, 53, 79, 94]
posicion = 33

resultado = busqueda_binaria(miLista, posicion)

if resultado != -1:
    print(f"El numero {posicion} se encuentra en la posición {resultado}.")
else:
    print(f"El numero {posicion} no se encuentra en la lista.")