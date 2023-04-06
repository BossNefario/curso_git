import sqlite3
conexao = sqlite3.connect ('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\atividadesemana4\\bdtarefa.sqlite3')
cursor = conexao.cursor()
sql_categoria = 'select id, categoria from categoria'
consulta = cursor.execute(sql_categoria)
for item in consulta:
    print("ID:", item[0], "Categoria:", item[1])
categoria_id = input('Digite qual o ID da categoria que deseja atualizar: ')
nova_categoria = input('Digite a nova categoria: ')
sql_nova_categoria = 'update categoria set categoria = ? where id = ?'
valores = [nova_categoria, categoria_id]
cursor.execute(sql_nova_categoria, valores)
conexao.commit()
conexao.close()