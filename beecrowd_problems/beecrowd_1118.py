'''resposta = 1
while resposta == 1:    
    nota1 = float(input())
    while nota1 > 10 or nota1 < 0:
        print('nota invalida')
        nota1 = float(input())
    nota2 = float(input())
    while nota2 > 10 or nota2 < 0:
        print('nota invalida')
        nota2 = float(input())
    media = (nota1 + nota2) / 2
    print(f'media = {media:.2f}')
    print('novo calculo (1-sim 2-nao)')
    resposta = int(input())
    if resposta == 1:
        print('novo calculo (1-sim 2-nao)')
    else:
        break'''

resposta = 1
while resposta == 1:    
    nota1 = float(input())
    while nota1 > 10 or nota1 < 0:
        print('nota invalida')
        nota1 = float(input())
    nota2 = float(input())
    while nota2 > 10 or nota2 < 0:
        print('nota invalida')
        nota2 = float(input())
    media = (nota1 + nota2) / 2
    print(f'media = {media:.2f}')
    while True:
        print('novo calculo (1-sim 2-nao)')
        resposta = int(input())
        if resposta == 1 or resposta == 2:
            break
    if resposta == 1:
        continue
    else:
        break