import random

def generar_lista_numeros(n, minimo, maximo):
    
    return [random.randint(minimo, maximo) for _ in range(n)]

def busqueda_secuencial(lista, objetivo):
    
    for numero in lista:
        if numero == objetivo:
            return True
    return False

n = 10
minimo = 1
maximo = 100
lista_numeros = generar_lista_numeros(n, minimo, maximo)

numeroBuscado = int(input("Ingresa un número para buscar en la lista de números aleatorios: "))

if busqueda_secuencial(lista_numeros, numeroBuscado):
    print(f"El número {numeroBuscado} está en la lista de números generados.")
else:
    print(f"El número {numeroBuscado} no está en la lista de números generados.")