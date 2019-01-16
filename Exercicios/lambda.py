def askInt():
    while True:
        try:
            num = int(input("Digite um número: "))
        except:
            print("Você não digitou um número!")
            continue
        return num

x = askInt()
y = askInt()

print("Operação (1/2/3/4)\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO: \n")
escolha = askInt()

while True:
    if escolha == 1:
        operacao = lambda x, y: x + y
    elif escolha == 2:
        operacao = lambda x, y: x - y
    elif escolha == 3:
        operacao = lambda x, y: x * y
    elif escolha == 4:
        try:
            operacao = lambda x, y: x / y
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Divisão por zero não é permitido")
            break

    print("Resultado: {}".format(operacao(x, y)))



