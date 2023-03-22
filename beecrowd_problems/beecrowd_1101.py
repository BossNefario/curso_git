while True:
    numero1, numero2 = map(int, input().split())
    soma = 0
    if numero1 <= 0 or numero2 <= 0:
        break
    elif numero1 > numero2:
        temp = numero1
        numero1 = numero2
        numero2 = temp
    for i in range(numero1, (numero2 + 1)):
        print(i, end='')
        soma += i
        if i < numero2:
            print(' ', end='')
    print(f' Sum={soma}')