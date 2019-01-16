from functools import reduce

f = lambda x,y: x+y


lst = [3, 4, 5, 6]



soma = reduce(f, lst)

print(soma)