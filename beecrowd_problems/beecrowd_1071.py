numero1 = int(input())
numero2 = int(input())
soma = 0
if numero1 > numero2:
    temp = numero1
    numero1 = numero2
    numero2 = temp
for i in range(numero1 + 1, numero2):
    if i % 2 != 0:
        soma += i
    else:
        pass
print(soma)