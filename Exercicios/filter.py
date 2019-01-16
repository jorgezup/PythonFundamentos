lista = [10, 11, 23, 25, 33, 35, 36, 72, 45]

a = list(filter(lambda num: num>24, lista))

print(a)
print("\n")

nomes = ('jorge', 'joão', 'pedro', 'maria', 'josé', 'regina', 'francisco')

for nome in nomes:
    for letra in nome:
        if letra[0] == 'j':
            print(nome)
print("\n")

filtro = list(filter(lambda pos: pos[0] == 'j', nomes))

print(len(filtro))
print(filtro)