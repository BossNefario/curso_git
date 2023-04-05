import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\bancom2s4.sqlite3')
cursor = conexao.cursor()
pedido_id = input("Qual o ID do pedido? ")
sql = "select sum(quantidade) from item_pedido where pedido_id = ?"
consulta = cursor.execute(sql, [pedido_id])
for resultado in consulta:
    print(resultado)
conexao.commit()
conexao.close()