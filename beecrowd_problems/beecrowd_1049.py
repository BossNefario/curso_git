classe = input()
familia = input()
genero = input()
if classe == 'vertebrado':
    if familia == 'ave':
        if genero == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if genero == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if familia == 'inseto':
        if genero == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if genero == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
