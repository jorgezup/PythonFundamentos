class Calculadora():
    def __init__(self):
        pass

    def soma(self, num1, num2):
        return num1+num2


    def subtracao(self, num1, num2):
        return num1-num2


    def multiplicacao(self, num1, num2):
        return num1*num2


    def divisao(self, num1, num2):
        return num1/num2

calc = Calculadora()

#operacao = int(input("Digite qual a operação: "))
n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

#calc.operacao(operacao)

soma = calc.soma(n1, n2)
sub = calc.subtracao(n1, n2)
mult = calc.multiplicacao(n1, n2)
divi = calc.divisao(n1, n2)


print(soma)
print(sub)
print(mult)
print(divi)

