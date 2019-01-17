from pymongo import MongoClient

#Realiza a conexão
conn = MongoClient('localhost', 27017)

#Cria um banco de dados
# ****** É apenas uma definição,
# a criação é feita ao inserir o primeiro dado
db = conn.cadastrodb

#Similar a uma tabela em SQL
colletiction = db.cadastrodb

########

import datetime

#cria um documento, um dicionário
post1 = {"codigo": "ID-99887725",
         "prod_name":"Geladeira",
         "marcas":["brastemp", "consul", "electrolux"],
         "data_cadastro":datetime.datetime.utcnow()}

#Inserir na colletion
colletiction = db.posts

#Inserção, insert_one
post_id = colletiction.insert_one(post1)

print(post_id.inserted_id)

#Dicionário 2, segundo documento; Registro
post2 = {"codigo": "ID-882233",
         "prod_name": "Televisor",
         "marcas": ["LG", "Samsung", "TCL"],
         "data_cadastro": datetime.datetime.utcnow()}

colletiction = db.posts

post_id = colletiction.insert_one(post2).inserted_id

print(post_id)

a = colletiction.find_one({"prod_name": "Televisor"})

print(a)

for post in colletiction.find():
    print(post)

print(db.name)

print(db.collection_names())