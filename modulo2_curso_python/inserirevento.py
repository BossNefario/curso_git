import sqlite3

conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancosem3.sqlite3')

cursor = conexao.cursor()

descricao = input('Digite a descrição do Evento: ')

data = input('Digite a data do evento: ')

sql = 'select id, descricao from categoria'
categorias = cursor.execute(sql)
print('Categorias disponíveis: ')
for categoria in categorias:
    print('ID:', categoria[0], 'Descrição:', categoria[1])

categoria_id = input("Digite o ID da categoria desejada: ")

sql = 'insert into evento (descricao, data, categoria_id) values (?, ?, ?)'

valores = [descricao, data, categoria_id]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()