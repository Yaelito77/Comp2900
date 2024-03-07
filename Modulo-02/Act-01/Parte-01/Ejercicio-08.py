def contar_vocales(cadena):
    cadena = cadena.lower()

    cantidad_vocales = sum(1 for letra in cadena if letra in "aeiou")
    return cantidad_vocales
    
cadena_ejemplo = "Dimelo que esta pasando!"
cantidad_vocales = contar_vocales(cadena_ejemplo)
print(f"La cantidad de vocales en la cadena es: {cantidad_vocales}")