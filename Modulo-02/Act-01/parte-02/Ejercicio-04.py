array = [6, 13, 64, 3, 76, 88, 32]

elemento_buscar = 76

posicion = -1

for n in range(len(array)):
    if array[n] == elemento_buscar:
        posicion = n
        break

if posicion != -1:
    print(f"El elemento {elemento_buscar} se encuentra en la posicion {posicion}")
else:
    print(f"El elemento {elemento_buscar} no se encuentra en el arreglo.")