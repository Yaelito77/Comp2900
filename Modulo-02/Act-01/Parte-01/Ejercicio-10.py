def contar_apariciones_letra(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

cadena = input("Ingrese una oracion: ")
letra = input("Ingrese la letra que desea buscar: ")

cantidad = contar_apariciones_letra(cadena, letra)
print(f"La letra '{letra}' aparece {cantidad} veces en la oracion.")