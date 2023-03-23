n = int(input())
minha_lista = []
for i in range(n):
    comando = input()
    if 'insert' in comando:
        chave, posicao, numero = comando.split()
        posicao = int(posicao)
        numero = int(numero)
        minha_lista.insert(posicao, numero)
    elif 'print' in comando:
        print(minha_lista)
    elif 'remove' in comando:
        chave, numero = comando.split()
        numero = int(numero)
        minha_lista.remove(numero)
    elif 'sort' in comando:
        minha_lista.sort()
    elif 'pop' in comando:
        minha_lista.pop()
    elif 'reverse' in comando:
        minha_lista.reverse()
    elif 'append' in comando:
        chave, numero = comando.split()
        numero = int(numero)
        minha_lista.append(numero)
    else:
        pass


