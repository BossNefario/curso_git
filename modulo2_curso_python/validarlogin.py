import sqlite3
import hashlib

conexao = sqlite3.connect('C:\\Users\\preis\\OneDrive\\Documentos\\01) Bruno\\Curso_GIT\\curso_git\\modulo2_curso_python\\masterclasssem4.sqlite3')
cursor = conexao.cursor()

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')

sql = 'select count(1) from usuario where email = ? and senha = ?'

senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

valores = [email, senha]
consulta = cursor.execute(sql, valores)

existe = 0
for resultado in consulta:
    existe = resultado[0]

if existe > 0:
    print('Usuário existe')
else:
    print('Usuário não existe')
