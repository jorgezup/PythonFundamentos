class Estudantes():
    def __init__(self):

        print("Classe criada")

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

estudante = Estudantes()

estudante.setNome("Jorge")

print(estudante.getNome())

#verifica se tem atributo
print(hasattr(estudante, "nome"))

#seta um valor novo ao atributo
setattr(estudante, "nome", "maria")

#pega o valor
print(getattr(estudante, "nome"))

#deleta o atributo
delattr(estudante, "nome")




