def promedio(lista_numero)
    suma = 0
    array_len = 0
    for valor in lista_numero:
        suma = suma + valor
        array_len = array_len + 1
    return (suma / array_len)


lst = [15, 65, 76, 23, 16, 34, 72, 12]
average = Average(lst)
print(lst)
print(f"El promedio de la lista es {average}")