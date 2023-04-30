import sqlite3
conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\exercicioemgrupoaula2\\bdeventos.sqlite3')
cursor = conexao.cursor()

sql = '''
CREATE TABLE organizador (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT (100) NOT NULL,
    email TEXT (100) NOT NULL,
    cpf TEXT (11) NOT NULL,
    CONSTRAINT organizador_UN UNIQUE (cpf)
)
'''

cursor.execute(sql)

sql = '''
CREATE TABLE eventos (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT (100) NOT NULL,
    organizador_id INTEGER NOT NULL,
    data TEXT (10) NOT NULL,
    local TEXT (100) NOT NULL,
    CONSTRAINT organizador_FK FOREIGN KEY (organizador_id) REFERENCES organizador(id)
    )
'''

cursor.execute(sql)

sql = '''
CREATE TABLE organizador_eventos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    evento_id INTEGER NOT NULL,
    organizador_id INTEGER NOT NULL,
    CONSTRAINT org_FK FOREIGN KEY (organizador_id) REFERENCES organizador(id),
    CONSTRAINT event_FK FOREIGN KEY (evento_id) REFERENCES evento(id)
)
'''

cursor.execute(sql)

conexao.commit()
conexao.close()