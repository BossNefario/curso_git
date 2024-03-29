import sqlite3
conexao = sqlite3.connect ('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\atividadesemana4\\bdtarefa.sqlite3')

sql_categoria = '''
CREATE TABLE categoria (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	categoria TEXT(100) NOT NULL
);
'''

cursor = conexao.cursor()
cursor.execute(sql_categoria)


sql_tarefa = '''
CREATE TABLE tarefa (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	categoria_id INTEGER NOT NULL,
	tarefa TEXT(100) NOT NULL,
    "data" TEXT(10) NOT NULL,
    status TEXT(20),
    CONSTRAINT pedido_FK FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
'''
cursor = conexao.cursor()
cursor.execute(sql_tarefa)


conexao.commit()
conexao.close()