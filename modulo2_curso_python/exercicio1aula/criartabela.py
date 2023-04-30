import sqlite3

conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\exercicio1aula\\bdfuncionarios.sqlite3')
cursor = conexao.cursor()

sql = '''
CREATE TABLE funcionarios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100) NOT NULL,
    cpf TEXT(11) NOT NULL,
    data_cadastro TEXT(10),
    endereco TEXT(100),
    CONSTRAINT organizador_UN UNIQUE (cpf)
);
'''
conexao.execute(sql)
conexao.commit()
conexao.close()