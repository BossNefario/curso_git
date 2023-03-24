import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancoexercicios.sqlite3')
cursor = conexao.cursor()
sql = '''
CREATE TABLE organizador (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50) NOT NULL,
    email TEXT(50) NOT NULL,
    cpf TEXT(11) NOT NULL,
    CONSTRAINT organizador_UN UNIQUE (cpf)
);
'''
cursor.execute(sql)
conexao.commit()

sql = '''
CREATE TABLE evento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	titulo TEXT(50) NOT NULL,
	organizador_id INTEGER NOT NULL,
	"data" TEXT(10) NOT NULL,
	local TEXT(50) NOT NULL,
	CONSTRAINT organizador_FK FOREIGN KEY (organizador_id) REFERENCES organizador(organizador)
);
'''
cursor.execute(sql)
conexao.commit()

conexao.close()