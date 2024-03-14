def contar_apariciones(arreglo, elemento):
    contador = 0
    for num in arreglo:
        if num == elemento:
            contador += 1
    return contador

numeros = [2, 8, 13, 23, 8, 31, 8] 
elemento_a_contar = 8  
    
cantidad_apariciones = contar_apariciones(numeros, elemento_a_contar)
    
print("El numero", elemento_a_contar, "aparece", cantidad_apariciones, "veces en el arreglo.")