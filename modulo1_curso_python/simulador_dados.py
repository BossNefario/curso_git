from random import randint
quantidade = int(input("Digite a quantidade de dados: "))
tentativa = 1
total = 0
while tentativa <= quantidade:
    valor = randint(1,6)
    print(valor)
    total = total + valor
    tentativa = tentativa + 1
print("Total: ", total)
print("Média: ", total / quantidade)
print("FIM DO PROGRAMA")