def eliminar_elemento(arreglo, elemento):

    if elemento in arreglo:
        arreglo.remove(elemento)
        return arreglo
    else:
        print("El elemento no se encuentra en el arreglo.")
        return arreglo

numeros = [2, 8, 13, 23, 31]

elemento_a_eliminar = 2
arreglo_modificado = eliminar_elemento(numeros, elemento_a_eliminar)

print("Arreglo original:", numeros)
print("Arreglo con el elemento eliminado:", arreglo_modificado)