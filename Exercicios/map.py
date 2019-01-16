from functools import reduce

f = lambda x,y: x+y

x = [2, 3]
y = [4, 6]



soma = list(map(f, x, y))


print(soma)

