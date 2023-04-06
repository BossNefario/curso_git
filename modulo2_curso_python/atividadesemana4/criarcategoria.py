import sqlite3
conexao = sqlite3.connect ('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\atividadesemana4\\bdtarefa.sqlite3')

cursor = conexao.cursor()

categoria = input('Digite a descrição da categoria: ')

sql = 'insert into categoria (categoria) values (?)'

valores = [categoria]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()