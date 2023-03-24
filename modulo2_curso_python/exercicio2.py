import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\bancoexercicios.sqlite3')
cursor = conexao.cursor()
sql = '''
CREATE TABLE organizador (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    cpf TEXT(11) NOT NULL,
    CONSTRAINT organizador_UN UNIQUE (cpf)
);
'''
cursor.execute(sql)
conexao.commit()

sql = '''
CREATE TABLE evento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	titulo VARCHAR(50) NOT NULL,
	organizador_id INTEGER NOT NULL,
	"data" VARCHAR(10) NOT NULL,
	local VARCHAR(50) NOT NULL,
	CONSTRAINT organizador_FK FOREIGN KEY (organizador_id) REFERENCES organizador(id)
);
'''
cursor.execute(sql)
conexao.commit()

sql = '''
CREATE TABLE organizador_evento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	organizador_id INTEGER NOT NULL,
	evento_id INTEGER NOT NULL,
	CONSTRAINT org_FK FOREIGN KEY (organizador_id) REFERENCES organizador(id)
    CONSTRAINT event_FK FOREIGN KEY (evento_id) REFERENCES evento(id)
);
'''
cursor.execute(sql)
conexao.commit()

conexao.close()