def numero_entero(cadena):
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())

cadena = "3654"
print(numero_entero(cadena))

cadena = "-6573"
print(numero_entero(cadena))

cadena = "14.73"
print(numero_entero(cadena))

cadena = "Hola mundo"
print(numero_entero(cadena))