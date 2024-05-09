import random

def generar_lista_numeros(n, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(n)]

def ordenar_lista(lista):
    return sorted(lista)

def busqueda_binaria_insertar(lista, valorObjetivo):
    
    inicio = 0
    fin = len(lista)

    while inicio < fin:
        medio = (inicio + fin) // 2
        if lista[medio] < valorObjetivo:
            inicio = medio + 1
        else:
            fin = medio

    return inicio

n = 10
minimo = 1
maximo = 100
listaNumeros = generar_lista_numeros(n, minimo, maximo)
listaOrdenada = ordenar_lista(listaNumeros)

numero_buscado = int(input("Ingresa un número para buscar en la lista ordenada de números aleatorios: "))

posicion = busqueda_binaria_insertar(listaOrdenada, numero_buscado)

if posicion < len(listaOrdenada) and listaOrdenada[posicion] == numero_buscado:
    print(f"El número {numero_buscado} se encuentra en la lista en la posición {posicion}.")
else:
    print(f"El número {numero_buscado} no se encuentra en la lista. Debería insertarse en la posición {posicion} para mantener la lista ordenada.")