import sqlite3
import random
import time
import datetime

######Definições######
#######Cria o banco
db = "produtos.db"
#######Realiza a conexão
conn = sqlite3.connect(db)
#######Cria um cursor
cur = conn.cursor()
#################################

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS produtos("
                "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                "nome_produto VARCHAR(100),"
                "valor_produto REAL,"
                "data TEXT)")
    print("Tabela criada com sucesso!!\n\n")

def le_quantidade():
    valor = int(input("Quantos produtos quer cadastrar? "))
    cont = 0
    while cont < valor:
        produto_input = input("Digite o nome: ")
        valor_input = input("Digite o valor: ")
        data = datetime.datetime.now()
        data_insert(produto_input, valor_input, data)
        cont += 1

    fecha_conexao()

def data_insert(nome_produto, valor_produto, data):

    cur.execute("INSERT INTO produtos (nome_produto, valor_produto, data) VALUES (?, ?, ?)",
                    (nome_produto, valor_produto, data))

def fecha_conexao():
    conn.commit()
    cur.close()
    conn.close()


def main():
    create_table()
    le_quantidade()


if __name__ == '__main__':
    main()



