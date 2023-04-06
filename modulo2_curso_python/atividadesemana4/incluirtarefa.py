import sqlite3
import datetime
conexao = sqlite3.connect ('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\atividadesemana4\\bdtarefa.sqlite3')
cursor = conexao.cursor()
sql = 'select * from categoria'
consulta = cursor.execute(sql)
for item in consulta:
    print('ID', item[0], 'Categoria', item[1])
categoria_id = input('Digite o ID da categoria para a tarefa: ')
tarefa = input('Digite a tarefa que entrará na lista: ')
hoje = datetime.date.today()
sql_tarefa = 'insert into tarefa (categoria_id, tarefa, data) values (?, ?, ?)'
valores = [categoria_id, tarefa, hoje]
cursor.execute(sql_tarefa, valores)
conexao.commit()
conexao.close()