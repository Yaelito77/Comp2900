arreglo = [3, 6, 4, 8, 14, 5]

maximo = arreglo[0]

for elemento in arreglo:
    if elemento > maximo:
        maximo = elemento

print(f"El maximo elemento del arreglo es: {maximo}")