import timeit

def max_lista(lista):
    return max(lista)

# Enfoque 2: Recorriendo la lista y comparando cada número con un valor
# de referencia para encontrar el número más grande
def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Crear una lista de números del 1 al 1000
numbers = list(range(1, 1001))

# Medir el tiempo de ejecución del Enfoque 1
time_max_lista =timeit.timeit(lambda: max_lista(numbers), number=10000)
print("Enfoque 1: ", time_max_lista)

# Medir el tiempo de ejecución del Enfoque 2
time_max_iterativo =timeit.timeit(lambda: max_iterativo(numbers),number=10000)
print("Enfoque 2: ", time_max_iterativo)