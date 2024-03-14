def calcular_promedio(arreglo):
    if len(arreglo) == 0:
        return 0
    
    suma = sum(arreglo)
    promedio = suma / len(arreglo)
    return promedio

numeros = [2, 8, 13, 23, 31]
promedio = calcular_promedio(numeros)
print("El promedio de los elementos del arreglo es:", promedio)