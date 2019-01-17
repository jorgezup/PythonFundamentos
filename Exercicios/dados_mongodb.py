import pymongo

#cria a conexão, por padrão já pega localhost 27017
client_conn = pymongo.MongoClient()

#lista todos od bancos
print(client_conn.database_names())

#define o objeto db
db = client_conn.cadastrodb

#Criando uma coleção
#db.create_collection("mycollection")

##Lista as coleções disponíveis
print(db.collection_names())

#Insere um documento na coleção criada
db.mycollection.insert_one({
    'titulo': 'MongoDB com Python',
    'descricao': 'MongoDB é um Banco de Dados no SQL',
    'by': 'Data Science Academy',
    'url': 'https://dsa.com.br',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'likes': 100
})

print(db.mycollection.find_one())

#Preparando um dicionário
doc1 = {"Nome": "Jorge",
        "sobrenome": "Zupirolli",
        "Instagran": "jzupirolli"}

#Inserirndo um documento
db.mycollection.insert_one(doc1)

#Preparando um documento
doc2 = {"Site": "https://www.sedfor.ufms.br",
        "Facebook": "facebook.com/eadufms"}

#inserindo um documento
db.mycollection.insert_one(doc2)

#Retornando os documentos da coleção
for rec in db.mycollection.find():
    print(rec)

#Conectando a uma coleção
collec = db["mycollection"]

#Contando os documentos de uma coleção
print(collec.count())

#Encontrando um único documento
redoc = collec.find_one()

print(redoc)

