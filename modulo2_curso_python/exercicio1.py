import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancoexercicios.sqlite3')
cursor = conexao.cursor()
sql = '''
CREATE TABLE categoria (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (100) NOT NULL
);
'''
cursor.execute(sql)
conexao.commit()

sql = '''
CREATE TABLE tafera (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(50) NOT NULL,
	categoria_id INTEGER NOT NULL,
	"data" VARCHAR (10),
	status Bool NOT NULL,
		CONSTRAINT tafera_FK FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
'''
cursor.execute(sql)
conexao.commit()

conexao.close()