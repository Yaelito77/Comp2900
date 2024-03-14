def encontrar_maximo(arreglo):
    maximo = arreglo[0]
    for elemento in arreglo:
        if elemento > maximo:
            maximo = elemento
    return maximo

arreglo = [12, 43, 17, 9, 8]

maximo_elemento = encontrar_maximo(arreglo)\

print(f"El maximo elemento en el arreglo es: {maximo_elemento}")