def dividir(a, b):
    assert b != 0
    return a / b

resultado = dividir(10, 0) # 0 va a dar un AssertionError

print(resultado)