import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancoexercicios.sqlite3')
cursor = conexao.cursor()
sql = '''
CREATE TABLE categoria (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50) NOT NULL
);
'''
cursor.execute(sql)
conexao.commit()

sql = '''
CREATE TABLE tafera (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50) NOT NULL,
	categoria_id INTEGER,
	"data" TEXT(10),
	status TEXT(15) NOT NULL,
	CONSTRAINT tafera_FK FOREIGN KEY (categoria_id) REFERENCES categoria(categoria)
);
'''
cursor.execute(sql)
conexao.commit()

conexao.close()