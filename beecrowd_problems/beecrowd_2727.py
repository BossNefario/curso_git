# Codigo Secreto
'''
while True:
    try:
        qtde_letras = int(input())
        glossario = {'.' : "a", '..' : 'b', '...' : 'c', '. .' : 'd', '.. ..' : 'e',
                '... ...' : 'f', '. . .' : 'g', '.. .. ..' : 'h', '... ... ...' : 'i',
                '. . . .' : 'j', '.. .. .. ..' : 'k', '... ... ... ...' : 'l',
                '. . . . .' : 'm', '.. .. .. .. ..' : 'n', '... ... ... ... ...' : 'o',
                '. . . . . .' : 'p', '.. .. .. .. .. ..' : 'q', '... ... ... ... ... ...' : 'r',
                '. . . . . . .' : 's', '.. .. .. .. .. .. ..' : 't', '... ... ... ... ... ... ...' : 'u',
                '. . . . . . . .' : 'v', '.. .. .. .. .. .. .. ..' : 'w', '... ... ... ... ... ... ... ...' : 'x',
                '. . . . . . . . .' : 'y', '.. .. .. .. .. .. .. .. ..' : 'z'}
        minha_lista = []
        while qtde_letras != 0:
            entrada = input()
            minha_lista.append(glossario[entrada])
            qtde_letras -= 1
        for item in minha_lista:
            print(item)
    except EOFError:
        break    
'''
'''
while True:
    try:
        alf = 'abcdefghijklmnopqrstuvwxyz'
        n = int(input())
        saida = ''
        while n > 0:
            l = input().split()
            pos = len(l[0]) + 3*(len(l)-1)
            saida += alf[pos-1]
            n -= 1
        for n in saida:
            print(n)
    except EOFError:
        break
'''