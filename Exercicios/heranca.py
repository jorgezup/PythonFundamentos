class Pessoa():
    def __init__(self):
        print("Pessoa criada")

    def Identif(self):
        print("Pessoa")

    def comer(self):
        print("Comendo")

class Homem(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        print("Homem criado")

    def Identif(self):
        print("Homem")

    def andar(self):
        print("Andando..")

jorge = Homem()
print(jorge.Identif())
