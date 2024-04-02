def potencia(base, exponente):
    
    if exponente < 0:
        return ("El exponente no puede ser un numnero negativo.")

    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Entre la base: "))
exponente = int(input("Entre el exponente: "))


resultado = potencia(base, exponente)

print(f"El {base} elevado a la {exponente} es: {resultado}")