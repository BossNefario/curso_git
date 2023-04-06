import sqlite3
import datetime
conexao = sqlite3.connect ('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\atividadesemana4\\bdtarefa.sqlite3')
cursor = conexao.cursor()
sql_consulta = 'select * from tarefa'
consulta = cursor.execute(sql_consulta)
for item in consulta:
    print('ID', item[0],'Categoria_ID', item[1], 'Tarefa', item[2], 'Data', item[3], 'Status', item[4])
conexao.commit()
conexao.close()