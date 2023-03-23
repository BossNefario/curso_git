seq = 10
maior = 0
contagem = 0
pos = 0
while seq > 0:
    numero = int(input())
    contagem += 1
    if numero > maior:
        maior = numero
        pos = contagem
    else:
        pass
    seq -= 1
print(maior)
print(pos)
