def lista(numeros):
    total = sum(numeros)
    cantidad = len(numeros)
    promedio = total / cantidad
    return promedio

lista_numeros = [34, 54, 12,76, 4, 32]

promedio = lista(lista_numeros)

print(f"El promedio de los numeros es: {promedio}")