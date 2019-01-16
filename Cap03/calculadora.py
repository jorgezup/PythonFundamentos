print("*"*10)
print("Python Calculator")
print("*"*10)

print("Selecione o número da operação desejado: ")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")

escolha =int(input("Escolha uma operação (1/2/3/4): "))

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if escolha == 1:
    operacao = n1 + n2
    print("SOMA: {} + {} = {}".format(n1, n2, operacao))

elif escolha == 2:
    operacao = n1 - n2
    print("SUBTRAÇÃO: {} - {} = {}".format(n1, n2, operacao))

elif escolha == 3:
    operacao = n1 * n2
    print("MULTIPLICAÇÃO: {} * {} = {}".format(n1, n2, operacao))

elif escolha == 4:
    operacao = n1 / n2
    print("DIVISÃO: {} / {} = {:.2f}".format(n1, n2, operacao))

else:
    print("Operação Inválida")


