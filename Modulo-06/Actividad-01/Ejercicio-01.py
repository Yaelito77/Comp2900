def busqueda_secuencial(lista, objetivo):
    
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

miLista = [7, 3, 1, 14, 9, 5]
numero = 16
resultado = busqueda_secuencial(miLista, numero)

if resultado != -1:
    print(f"El numero {numero} se encuentra en la posición {resultado}.")
else:
    print(f"El numero {numero} no se encuentra en la lista.")