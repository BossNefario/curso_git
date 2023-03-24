import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancoexercicios.sqlite3')
cursor = conexao.cursor()
sql = '''
CREATE TABLE tarefas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50),
	categoria_id INTEGER,
	"data" TEXT(10),
	status TEXT(15)
);
'''

cursor.execute(sql)
conexao.commit()
conexao.close()