import sqlite3
import hashlib

conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\masterclasssem4.sqlite3')
cursor = conexao.cursor()

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
while True:
    senha = input('Digite sua senha: ')
    confirma_senha = input('Confirme sua senha: ')
    if senha == confirma_senha:
        break
    else:
        print('A confirmação de senha está errada!')

sql = 'insert into usuario (nome, email, senha) values (?, ?, ?)'

senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
valores = [nome, email, senha]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()