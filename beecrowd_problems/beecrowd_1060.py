seq = 6
positivo = 0
while seq > 0:
    n = int(input())
    if n > 0:
        positivo += 1
        seq -= 1
    else:
        seq -= 1
print(positivo,'numeros positivos')

