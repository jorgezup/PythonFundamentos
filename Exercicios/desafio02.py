def askNum():
    while True:
        try:
            num = int(input())
        except:
            break
        return num

num = askNum()
lst_primos = [False, False]


for numero in range(2,num):
    isPrime = True
    print("numero->",numero)
    for n in range(2, numero):
        print("n->", n)
        if numero % n == 0:
            print("falso%2->", numero)
            isPrime = False

    if isPrime:
        lst_primos.append(True)
    else:
        lst_primos.append(False)

print(lst_primos)

