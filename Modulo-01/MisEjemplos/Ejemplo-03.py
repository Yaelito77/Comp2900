def suma(a, b):
    return (a + b) #------ Retorna ;a suma de a + b

resultado = suma(5, 4) #-- Llamar a la funcion y recibir el resultado

print(F"La suma es de: {resultado}") #-------- Imprimir el resultado 
print("")

#----------------------------------------------------------------------------

def otrosuma(a=0, b=0):
    return (a + b)

resultado = otrosuma(10, 5)
print(resultado)

resultado = otrosuma()
print(resultado)

resultado = otrosuma(11)
print(resultado)


print("")
#-----------------------------------------------------------------------------

def resta(a ,b):
    return (a - b)

print("Para restar...")
print("")

primerNum = int(input("Entre el primer numero: "))

segundonum = int(input("Entre el segundo numero: "))

respuesta = resta(primerNum, segundonum)
print("")
print(f"La resta de los numeros es: {respuesta}")
print("")