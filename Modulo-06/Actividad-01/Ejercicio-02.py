def busqueda_secuencial(lista, palabra):
    
    for palabraLista in lista:
        if palabraLista == palabra:
            return True
    return False

listaPalabras = ["guineo", "uva", "mofongo", "china", "melon"]
palabraBuscada = "platanutre"

if busqueda_secuencial(listaPalabras, palabraBuscada):
    print(f"La palabra '{palabraBuscada}' está en la lista de palabras.")
else:
    print(f"La palabra '{palabraBuscada}' no está en la lista de palabras.")