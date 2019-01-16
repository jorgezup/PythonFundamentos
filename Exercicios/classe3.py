class Cachorro():
    def __init__(self, raca, dt_nasc):
        self.raca = raca
        self.dt_nasc= dt_nasc
        print("Construtor criado")

Rex = Cachorro('Labrador', 2009)
Princesa = Cachorro(raca='Poodle', dt_nasc=2010)


print(Rex.raca, Rex.dt_nasc)
print(Princesa.raca)
print(Rex)