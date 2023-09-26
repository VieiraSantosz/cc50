1° pip install mysql-connector-python

2° Criar banco de dados no MySql
- CREATE DATABASE SeboOnline;
- USE SeboOnline;

3° Criar a tabela
- CREATE TABLE usuarios (
    idUser INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    status VARCHAR(10) NOT NULL,
    type VARCHAR(20) NOT NULL
);

- CREATE TABLE administradores (
    idAdmin INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    status VARCHAR(10) NOT NULL,
    type VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    area VARCHAR(20) NOT NULL
);

4° Código

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vieira1234',
    database='seboonline',
)

if conexao.is_connected():
    print("Conexão ao MySQL bem-sucedida!")
    
else:
    print("Não foi possível conectar com o MySql!!")
    
conexao.close()


### ADICIONA AS INFO NO BANCO DE DADOS ###
cursor = conexao.cursor()

nome    = "Vieira"
email   = "vieira@gmail.com"
senha   = "vieira1234"
status  = "ativo"
tipo    = "comprador"

comando = f'INSERT INTO usuarios (name, email, password, status, type) VALUES ("{nome}", "{email}", "{senha}", "{status}", "{tipo}")' 
cursor.execute(comando)

conexao.commit() # edita o seu banco de dados

cursor.close()
conexao.close()
#########################################


### LER AS INFO DO BANCO DE DADOS ###
cursor = conexao.cursor()

comando = 'SELECT * FROM usuarios' 
cursos.execute(comando)

resultado = cursor.fetchall() # lê o banco de dados
print(resultado)

cursor.close()
conexao.close()
#############################################


### MUDAR AS INFO DO BANCO DE DADOS ### 
cursor = conexao.cursor()

nome    = "Vieira"
senha   = "santos1234"

comando = f'UPDATE usuarios SET name = "{nome}" WHERE password = "{senha}"' 
cursos.execute(comando)

conexao.commit() #edita o seu banco de dados

cursor.close()
conexao.close()
#########################################


### DELETAR AS INFO DO BANCO DE DADOS ###
cursor = conexao.cursor()

nome    = "Vieira"

comando = f'DELETE FROM usuarios WHERE name = "{nome}' 
cursos.execute(comando)

conexao.commit() #edita o seu banco de dados

cursos.close()
conexao.close()
###########################################