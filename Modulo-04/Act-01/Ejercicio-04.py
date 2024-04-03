def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
    
cadena = ["Amigo", "Maniobra", "Estornudo", "malestar"]

for cadena in cadena:
    resultado = invertir_cadena(cadena)
    print(f"La palabra {cadena} invertida es: {resultado}")
