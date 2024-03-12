def sumar_arreglo(arreglo):
    suma = 0
    for elemento in arreglo:
        suma += elemento
    return suma

arreglo = [1, 2, 3, 4,  5]

suma_total = sumar_arreglo(arreglo)

print(F"La suma total de los elementos del arreglo es: {suma_total}")