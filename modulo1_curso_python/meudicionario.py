meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
print(meu_dicionario['a'])
print(meu_dicionario['b'])
print(meu_dicionario['c'])
print(meu_dicionario)
meu_dicionario['d'] = 4
print(meu_dicionario['d'])
print(meu_dicionario)
print(meu_dicionario.get('e', -1))
print(meu_dicionario.get('e'))
print(meu_dicionario.get('d', -1))
print(list(meu_dicionario.items()))
print(list(meu_dicionario.keys()))
print(list(meu_dicionario.values()))
dic_listas = {'lista':[]}
item1 = input("Atribua um elemento a lista: ")
dic_listas['lista'].append(item1)
print(dic_listas)
remover = input("Digite uma chave para remover: ")
meu_dicionario.pop(remover)
print(meu_dicionario)
for chave,valor in meu_dicionario.items():
    print(f'Chave é {chave} e o valor é {valor}')