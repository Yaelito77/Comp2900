array = [45, 3, 12, 8, 11, 78, 50, 49]

for n in range(len(array)):
    for i in range(n + 1, len(array)):
        if array[n] > array[i]:
            array[n], array[i] = array[i], array[n]

print(f"El arreglo ordenado de mayor a menor es: {array}")