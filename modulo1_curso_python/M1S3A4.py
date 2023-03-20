"""soma = 0
numero = int(input())
while numero != -1:
    soma += numero
    numero = int(input())
print(soma)"""

def soma():
    soma = 0
    numero = int(input())
    while numero != -1:
        soma += numero
        numero = int(input())
    return soma
resultado = soma()
print(resultado)