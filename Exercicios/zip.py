a = [1, 3, 5]
b = [3, 5, 9]

print(list(zip(a, b)))

x = ['A', 'B', 'Z']
y = ['m', 'n']

print(list(zip(x, y)))

dicA = {'a':2, 'b':6}
dicB = {'c':3, 'd':9}

print(list(zip(dicA, dicB)))
print(list(zip(dicA, dicB.values())))
print(list(zip(dicA.values(), dicB.keys())))
