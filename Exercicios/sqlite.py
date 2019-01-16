import os

#verifica se o arquivo existe, caso exista, remove-o
if os.path.exists("usuarios.db"):
    os.remove("usuarios.db")
else:
    None

import sqlite3
#define o nome e o caminho do banco de dados
bd = "usuarios.db"

#realiza a conexão, passando o nome do banco
#se não encontrar o banco, o mesmo é criado
conn = sqlite3.connect(bd)

#cria um cursor para percorrer todos os registros no banco
cursor = conn.cursor()

#comando SQL para criação da tabela
sql_create = "create table usuarios" \
             "(id integer primary key," \
             "nome varchar(100)," \
             "sobrenome varchar(100)," \
             "email varchar(100))"

#chama o cursor e executa o sql
cursor.execute(sql_create)

#cria uma variável genérica de inserção
sql_insert = "insert into usuarios values (?, ?, ?, ?)"

#cria uma lista para inserir vários registros
#record set, conjunto de registros
#cada elemento da lista é uma tupla, e cada tupla tem 4 elementos
recset = [(1, "Jorge", "Zupirolli", "jorge.zupirolli@ufms.br"),
          (2, "Eiva", "da Silva", "eiva.quimica@gmail.com"),
          (3, "João", "Zupirolli", "joao.zupirolli@gmail.com")]

#para cada registro da lista, chama o cursor e executa a inserção
#chamando a variável genérica e a linha atual
for rec in recset:
    cursor.execute(sql_insert, rec)

#finaliza a transação
conn.commit()

#variável para realizar o select
sql_select = "select * from usuarios"

#executa o comando select
cursor.execute(sql_select)

#fetchall, pega todos os registros e salva na variável dados
dados = cursor.fetchall()

#para cada linha da variavel dados
for linha in dados:
    print("ID: {}\nNome: {}\nSobrenome: {}\nemail: {}\n"
          .format(linha[0], linha[1], linha[2], linha[3]))

#encerra o cursor
cursor.close()

#fecha a conexão
conn.close()