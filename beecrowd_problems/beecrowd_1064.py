seq = 6
positivo = 0
soma = 0
while seq > 0:
    n = float(input())
    if n > 0:
        positivo += 1
        soma += n
        seq -= 1
    else:
        seq -= 1
media = (soma / positivo)
print(positivo,'valores positivos')
print(f'{media:.1f}')
