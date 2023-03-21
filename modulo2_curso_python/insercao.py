import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\database.sqlite3')
cursor = conexao.cursor()

sql = '''
insert into categoria (descricao) values ('Celulares')
'''

cursor.execute(sql)
conexao.commit()
conexao.close()