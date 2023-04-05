import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\bancom2s4.sqlite3')
cursor = conexao.cursor()
sql = "select p.data from pedido as p, cliente as c where p.cliente_id = c.id and c.nome = 'Maria da Silva'"
consulta = cursor.execute(sql)
for resultado in consulta:
    print(resultado)
conexao.commit()
conexao.close()