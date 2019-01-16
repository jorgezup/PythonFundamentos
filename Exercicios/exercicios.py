class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


class MP3Player(Smartphone):
    def __init__(self, tamanho, interface, capacidade):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)


    def __str__(self):
        return ("Tamanho: {}\nInterface: {}"
                "\nCapacidade: {}".format(self.tamanho, self.interface, self.capacidade))


mp = MP3Player("10.1", "Android", "64Gb")


print(mp)