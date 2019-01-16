class Cha():
    def __init__(self, nome, qntd):
        self.nome = nome
        self.qntd = qntd

    def __str__(self):
        return ("o chá escolhido foi {} e a quantidade é: {}"
                .format(self.nome, self.qntd))


cha1 = Cha("Camomila", "2 colheres")
cha2 = Cha("Verde", "1 colher")

print(cha1)
print(cha2)