def eliminar_elemento(arreglo, elemento):
    if elemento in arreglo:
        arreglo_modificado = arreglo.copy()  # Crear una copia del arreglo original
        arreglo_modificado.remove(elemento)
        return arreglo_modificado
    else:
        print("El elemento no se encuentra en el arreglo.")
        return arreglo

numeros = [2, 8, 13, 23, 31]

elemento_a_eliminar = 8
arreglo_modificado = eliminar_elemento(numeros, elemento_a_eliminar)

print("Arreglo original:", numeros)
print("Arreglo con el elemento eliminado:", arreglo_modificado)