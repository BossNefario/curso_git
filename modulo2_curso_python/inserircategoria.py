import sqlite3

conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancosem3.sqlite3')

cursor = conexao.cursor()

descricao = input('Digite a descrição da catergoria: ')

sql = 'insert into categoria (descricao) values (?)'

valores = [descricao]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()