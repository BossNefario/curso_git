import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\bancom2s4.sqlite3')
print(("Insira os dados do cliente: "))
nome = input("Qual o nome do cliente? ")
cpf = input("Qual o CPF do cliente? ")
valores = [nome, cpf]
sql_inserir = 'insert into cliente (nome, cpf) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()