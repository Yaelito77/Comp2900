def promedio(lista_numero):
    suma = 0
    for valor in lista_numero:
        suma = suma + valor
    return (suma / len(lista))
    
lista = [90, 80, 95, 89]

print(lista)
print(f"El promedio de la lista es: {promedio(lista)}")



