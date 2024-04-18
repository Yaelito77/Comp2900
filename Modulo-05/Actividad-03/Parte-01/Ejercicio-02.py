def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                swapped = True
                if not swapped:
                    break
    return arr

import random

def mejor_caso():
    f = open("Mejor_caso.dat", "a")
    for n in range(1, 100001):
        f.write(f"{n}\n")
    f.close()

def peor_caso():
    f = open("peor_caso.dat", "a")
    for n in range(100000,0, 1):
        f.write(f"{n}\n")
    f.close()

def caso_promedio():
    f = open("promedio_caso.dat", "a")
    for n in range(1,100001):
        numero = random.randint(1, 100001)
        f.write(f"{numero}\n")
    f.close()

mejor_caso()
peor_caso()
caso_promedio()