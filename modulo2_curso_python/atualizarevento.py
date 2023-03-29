import sqlite3

conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancosem3.sqlite3')

cursor = conexao.cursor()

sql = 'select id, descricao, categoria_id, data from evento'

eventos = cursor.execute(sql)

for evento in eventos:
    print("ID:", evento[0], "Descrição:", evento[1], "Categoria ID:", evento[2], "Data:", evento[3])

evento_id = input('Digite o ID do evento que deseja atualizar: ')

descricao = input('Digite a nova descrição: ')
data = input('Digite a nova data: ')

sql = 'update evento set descricao = ?, data = ? where id = ?'

valores = [descricao, data, evento_id]

cursor.execute(sql, valores)
conexao.commit()
conexao.close()