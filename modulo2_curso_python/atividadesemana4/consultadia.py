import sqlite3
conexao = sqlite3.connect ('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\atividadesemana4\\bdtarefa.sqlite3')
cursor = conexao.cursor()
dia = input('Digite o dia que deseja verificar: (AAAA-MM-DD) ')
sql = 'select * from tarefa where data = ?'
valores = [dia]
consulta = cursor.execute(sql, valores)
for item in consulta:
    print('ID', item[0], 'Tarefa', item[2])
conexao.commit()
conexao.close()