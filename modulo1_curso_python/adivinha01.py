from random import randint
numero = randint (1, 50)
tentativas = 5
while tentativas > 0:
    chute = int(input("Digite um palpite: "))
    if chute == numero:
        print("Você acertou. Parabéns")
        break
    elif chute < numero:
        print("Você errou, o número é maior.")
    else:
        print("Você errou, o número é menor.")
    tentativas = tentativas - 1
print("FIM DO PROGRAMA")