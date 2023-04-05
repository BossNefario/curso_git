import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\database\\bancom2s4.sqlite3')
cursor = conexao.cursor()
pedido_id = input('Qual o IF do pedido que deseja remover? ')
sql = 'delete from pedido where id = ?'
valores = [pedido_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()