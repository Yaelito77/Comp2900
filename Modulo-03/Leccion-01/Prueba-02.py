from ejemplo02 import clasificar_numero

# Prueba
assert clasificar_numero(5) == "Positivo", "La clasificaciónno es correcta."
assert clasificar_numero(-3) == "Negativo", "La clasificaciónno es correcta."
assert clasificar_numero(0) == "Cero", "La clasificación no escorrecta."