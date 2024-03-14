def ordenar_arreglo(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]


numeros = [17, 3, 76, 5, 15] 
ordenar_arreglo(numeros)
print("Arreglo ordenado de menor a mayor:", numeros)