import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\bancom2s4.sqlite3')
cursor = conexao.cursor()
sql = "select * from cliente where nome like 'M%'"
consulta = cursor.execute(sql)
for resultado in consulta:
    print(resultado)
conexao.commit()
conexao.close()