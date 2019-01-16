nums = [10, 12, 14, 23, 54, 32, 78]

operacao = [x**2 for x in nums]

print(operacao)

op = [x for x in nums if x > 20]

print(op)

nomes = ['jorge', 'joão', 'pedro', 'josé', 'henrique', 'regina', 'maria', 'francisco']

filtro = [nome for nome in nomes if nome[0] == 'j']
print(filtro)
