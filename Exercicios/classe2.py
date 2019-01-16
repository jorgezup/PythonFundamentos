class Livro():
    def __init__(self, titulo, isbn, autor):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        print("Construtor criado")

    #def imprime(self, titulo, isbn, autor):
    def imprime(self):
        print("Livro: {}\nISBN: {}\nAutor: {}".format(self.titulo, self.isbn, self.autor))

livro = Livro("A Arte da Guerra", 776655, "Sun Tzu")
livro2 = Livro("O pode do Hábito", 887765, "JJAA")

livro.imprime()
print("\n")
livro2.imprime()