qtde = int(input())
dentro = 0
fora = 0
while qtde > 0:
    numero = int(input())
    if numero >= 10 and numero < 20:
        dentro += 1
        qtde -= 1
    else:
        fora += 1
        qtde -= 1
print(dentro, 'in')
print(fora, 'out')
