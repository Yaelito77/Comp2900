import random
def generar_numeros_aleatorios(cantidad, minimo, maximo):

    lista_numeros = []
    for _ in range(cantidad):
        numero_aleatorio = random.randint(minimo, maximo)
        lista_numeros.append(numero_aleatorio)

    return lista_numeros

cantidad = 5
minimo = 1
maximo = 100
lista_aleatoria = generar_numeros_aleatorios(cantidad, minimo, maximo)
print(f"Lista de numeros aleatorios: {lista_aleatoria}")