def saludo():
    global nombre 
    nombre = "John Doe"
    print(f"Hola {nombre}")

def despedida():
    #global nombre
    nombre = "Sarah swan"
    print(f"Adios {nombre}")

saludo()
despedida()
print(nombre)