nomes = ['jorge', 'joão', 'pedro', 'josé', 'henrique', 'regina', 'maria', 'francisco']

for i, nome in enumerate(nomes):
    print(i, nome)

for i, nome in enumerate(nomes):
    if nome == 'henrique':
        print(i)

filtro = [i for i, nome in enumerate(nomes) if nome == 'maria']
print(filtro)