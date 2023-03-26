numero, valor = input().split()
while numero != '0' and valor != '0':
    for i in valor:
        novo_valor = int(valor.replace(numero,''))
    print(novo_valor)
    numero, valor = input().split()