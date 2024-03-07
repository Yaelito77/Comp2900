array = [70, 43, 72, 12, 49, 29]

element_delete = 12

position = -1
for n in range(len(array)):
    if array[n] == element_delete:
        position = n
        break
if position != -1:
    del array[position]

    print(f"El elemento eliminado es: {element_delete}")
    print(f"Arreglo con el elemento eliminado: {array}")