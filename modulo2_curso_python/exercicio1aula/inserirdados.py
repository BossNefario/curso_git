import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\exercicio1aula\\bdfuncionarios.sqlite3')
cursor = conexao.cursor()
sql = '''
insert into funcionarios (nome, cpf) values ('Danilo', '11111111111')
'''

cursor.execute(sql)
conexao.commit()
conexao.close()