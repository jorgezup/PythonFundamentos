class Livro():

    ##Método construtor
    #Cria a classe
    def __init__(self):
        self.titulo = "O poder da mente"
        self.isbn = 909382798

        print("Construtor chamado")

    def imprime(self):
        print("Foi criado o livro  - {} \ncom isbn {}".format(self.titulo, self.isbn))

#instanciar a classe
#pode ser qualquer nome
#livro_teste objeto da classe Livro
livro_teste = Livro()

print(livro_teste.titulo)
print(livro_teste.isbn)
livro_teste.imprime()
