import timeit

def search_for(number, numbers):
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i 
        return -1
        
# Enfoque 2: usando la función index()
def search_index(number, numbers):
    try:
        return numbers.index(number)
    except ValueError:
        return -1
        
# Crear una lista de números del 1 al 1000
numbers = list(range(1, 1001))

random_number = 500

# Medir el tiempo de ejecución del Enfoque 1
time_search_for =timeit.timeit(lambda: search_for(random_number, numbers), number=10000)
print("Enfoque 1: ", time_search_for)

# Medir el tiempo de ejecución del Enfoque 2
time_search_index =timeit.timeit(lambda: search_index(random_number, numbers),number=10000)
print("Enfoque 2: ", time_search_index)