def rotar_arreglo_derecha(arreglo):
    if len(arreglo) <= 1:
        return arreglo  
    ultimo_elemento = arreglo[-1]
    for i in range(len(arreglo) - 1, 0, -1):
        arreglo[i] = arreglo[i - 1]
    arreglo[0] = ultimo_elemento
    return arreglo

numeros = [2, 8, 13, 23, 31]

arreglo_rotado = rotar_arreglo_derecha(numeros)
print("Arreglo con los elementos rotados a la derecha:", arreglo_rotado)