import timeit
import random

def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Enfoque 2: fórmula matemática para calcular la suma de
# una serie aritmética
def suma_formula(n):
    return (n * (n+1)) // 2

random_number = random.randint(1, 1000)

# Medir el tiempo de ejecución del Enfoque 1
time_suma_for =timeit.timeit(lambda: suma_for (random_number), number=10000)
print("Enfoque 1: ", time_suma_for)

# Medir el tiempo de ejecución del Enfoque 2
time_suma_formula =timeit.timeit(lambda: suma_formula(random_number),number=10000)
print("Enfoque 2: ", time_suma_formula)