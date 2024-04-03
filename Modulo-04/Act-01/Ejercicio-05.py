def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)
    
valores = [(7, 7), (9, 3), (12, 4), (7, 3)]

for n, k in valores:
    coeficiente = coeficiente_binomial(n, k)
    print(f"El coeficiente binominal de {n} tomado {k} a la vez es: {coeficiente}")
