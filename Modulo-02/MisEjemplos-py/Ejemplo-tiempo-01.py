import timeit

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= 1
    return resultado

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)
    
# Tiempo del enfoque iterativo
tiempo_iteractivo = timeit.timeit('factorial_iterativo(10)', globals=globals(), number=10000)
# Tiempo del enfoque recursivo
tiempo_reursivo = timeit.timeit('factorial_recursivo(10)', globals=globals(), number=10000)

print(f"Tiempo Iterativo: {tiempo_iteractivo} segundos.")
print(f"Tiempo Recursivo: {tiempo_reursivo} segundos.")