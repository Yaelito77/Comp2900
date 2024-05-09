def busqueda_binaria_insertar(lista, valor_objetivo):
    
    inicio = 0
    fin = len(lista)

    while inicio < fin:
        medio = (inicio + fin) // 2
        if lista[medio] < valor_objetivo:
            inicio = medio + 1
        else:
            fin = medio

    return inicio

miLista = [4, 6, 10, 14, 19, 27, 36, 55, 71, 99]
valor_objetivo = 42

posicion = busqueda_binaria_insertar(miLista, valor_objetivo)

print(f"El numero {valor_objetivo} debería insertarse en la posición {posicion} para mantener la lista ordenada.")