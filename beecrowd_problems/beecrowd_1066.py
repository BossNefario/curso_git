seq = 5
pares = 0
impares = 0
positivos = 0
negativos = 0
while seq > 0:
    n = int(input())
    if ((n % 2) == 0):
        pares += 1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            pass
        seq -= 1
    else:
        impares += 1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            pass
        seq -= 1
print(pares,'valor(es) par(es)')
print(impares,'valor(es) impar(es)')
print(positivos,'valor(es) positivo(s)')
print(negativos,'valor(es) negativo(s)')