def miFuncion():
    print ("Hola como estas? ")

miFuncion()

print("")

#-----------------------------------------------------------------------

def saludo(mensaje):
    print(f"Hace tiempo, {mensaje}!")

saludo ("No se de ti")

#-----------------------------------------------------------------------

def pedirNombre():
    global nombre
    nombre = input("diga su nombre: ")
    # return nombre
    
def pedirGpa():
    global gpa
    gpa = float(input("Diga su GPA: "))

#nombre = ""

print("Bienvenido")
pedirNombre()
pedirGpa()

print(f"Su nombre es {nombre} y su GPA es de {gpa}")

