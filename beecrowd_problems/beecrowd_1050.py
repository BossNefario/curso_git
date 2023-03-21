
meu_dicionário = {61 : 'Brasilia', 71 : 'Salvador', 11 : 'Sao Paulo', 21 : 'Rio de Janeiro', 
                32 : 'Juiz de Fora', 19 : 'Campinas',27 : 'Vitoria', 31 : 'Belo Horizonte'}
ddd = int(input())
if ddd in meu_dicionário:
    print(meu_dicionário[ddd])
else:
    print('DDD nao cadastrado')

'''
# Solução longa usando if

ddd = int(input())
if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
'''