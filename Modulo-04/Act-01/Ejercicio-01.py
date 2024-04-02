def suma_naturales(n):
    if n <= 0:
        return 0
    else:
        return n + suma_naturales(n - 1)
    
print(f"La suma de los primeros 5 numeros naturales es: {suma_naturales(5)}")
print(f"La suma de los primeros 10 numeros naturales es: {suma_naturales(10)}")
print(f"La suma de los primeros 15 numeros naturales es: {suma_naturales(15)}")