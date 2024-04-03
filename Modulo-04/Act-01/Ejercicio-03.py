def euclides_maximo_comun_divisor(a,b):
    if b == 0:
        return a
    else:
        return euclides_maximo_comun_divisor(b, a % b)
    
numeros = [(12, 24), (43, 86), (66, 118)]

for a, b in numeros:
    maximo_comun_divisor = euclides_maximo_comun_divisor(a,b)
    print(f"El maximo comun divisor de {a} y {b} es: {maximo_comun_divisor}")
