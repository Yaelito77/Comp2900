array = [12, 45, 78, 15, 7, 24]

last_array = array[-1]
for n in range(len(array) - 1, 0, -1):
    array[n] = array[n -1]

array[0] = last_array

print(f"El arreglo con los elementos rotados es: {array}")