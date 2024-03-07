def promedio(lista_numero):
    suma = 0
    array_lenghth = 0
    for valor in lista_numero:
        suma = suma + valor
        array_lenghth = array_lenghth + 1
    return (suma / array_lenghth)

lista = [12, 14, 15, 25, 36]
resultado = promedio(lista)

print(f"El resultado es: {resultado}")






#def lista(numeros):
#    total = sum(numeros)
#    cantidad = len(numeros)
#    promedio = total / cantidad
#    return promedio

#lista_numeros = [34, 54, 12,76, 4, 32]

#promedio = lista(lista_numeros)

#print(f"El promedio de los numeros es: {promedio}")