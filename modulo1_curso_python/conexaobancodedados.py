import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\database.sqlite3')
cursor = conexao.cursor()
sql = '''
create table categoria (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    descricao text(100)
)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()