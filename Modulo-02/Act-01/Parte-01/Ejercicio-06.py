import array

def invertir_cadena(cadena):
    array_length = len(cadena)
    nueva_cadena = ""
    for n in range(array_length):
        nueva_cadena += (cadena[array_length-1 -n])
    return nueva_cadena
    
mensaje = "Mensaje de prueba"
print(mensaje)
print(invertir_cadena(mensaje))