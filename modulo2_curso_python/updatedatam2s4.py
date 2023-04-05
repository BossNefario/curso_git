import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\bancom2s4.sqlite3')
cursor = conexao.cursor()
cliente_id = input('Qual o IF do Cliente que deseja atualizar? ')
nome = input("Informe o novo nome do cliente: ")
cpf = input('Informe o novo CPF do cliente: ')
sql = 'update cliente set nome = ?, cpf = ? where id = ?'
valores = [nome, cpf, cliente_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()