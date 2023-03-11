from random import randint
numero = randint (1, 100)
tentativas = 5
while tentativas > 0:
    chute = int(input("Digite um palpite: "))
    diferenca = numero - chute
    if chute == numero:
        print("Você acertou. Parabéns")
        break
    elif diferenca <= 5 and diferenca >= -5:
        print("Você errou, mas está quente.")
    elif diferenca > 0:
        print("Você errou, o número é maior.")
    else:
        print("Você errou, o número é menor.")
    tentativas = tentativas - 1
print("FIM DO PROGRAMA O NÚMERO ERA: ", numero)