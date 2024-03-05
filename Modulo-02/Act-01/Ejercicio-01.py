def maximo(num1, num2):
    if num1 > num2:
        return num1

    else:
        return num2
    
primer_numero = float(input("Entre el primer numero: "))
segundo_numero = float(input("Entre el segundo numero: "))

resultado = maximo(primer_numero, segundo_numero)

print(f"El numero maximo es: {resultado}")