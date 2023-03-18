dicionario_cliente = {}
seq = 5

while seq >= 1:
    dicionario_cliente['nome'] = input()
    dicionario_cliente['cpf'] = input()
    dicionario_cliente['idade'] = int(input())
    print("Cliente:", dicionario_cliente['nome'], "CPF:", dicionario_cliente['cpf'], "Idade:", dicionario_cliente['idade'])
    seq -= 1