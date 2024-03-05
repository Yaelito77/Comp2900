def fahrenheit_a_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return(celcius)

resultado = fahrenheit_a_celcius(54)

print(f"El grado de fahrenheit a celcius es: {resultado}")