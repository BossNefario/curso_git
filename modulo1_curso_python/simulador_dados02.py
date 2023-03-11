from random import randint
quantidade = int(input("Digite a quantidade de dados: "))
tentativa = 1
valores = []
while tentativa <= quantidade:
    valor = randint(1,6)
    print(valor)
    valores.append(valor)
    tentativa = tentativa + 1
print("TOTAL: ", sum(valores))
print("MÉDIA: ", sum(valores) / quantidade)
print("MAIOR: ", max(valores))
print("MENOR: ", min(valores))
print("FIM DO PROGRAMA")