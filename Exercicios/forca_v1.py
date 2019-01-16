import random

tabuleiro = ['''
>>>>>>> Jogo da Forca <<<<<<<

+=======+
|       |
        |
        |
        |
        |
        |
=========''', '''

+=======+
|       |
0       |
        |
        |
        |
        |
=========''', '''

+=======+
|       |
0       |
|       |
        |
        |
        |
=========''', '''

+=======+
|       |
0       |
|\      |
        |
        |
        |
=========''', '''

=+======+
 |      |
 0      |
/|\     |
        |
        |
        |
=========''', '''

=+======+
 |      |
 0      |
/|\     |
  \     |
        |
        |
=========''', '''

=+======+
 |      |
 0      |
/|\     |
/ \     |
        |
        |
=========''']


class Forca:

    #Recebe a apalavra sorteada
    def __init__(self, palavra):
        self.palavra = palavra
        self.listaCorretas = []
        self.listaErradas = []
        print(self.palavra)

    #Verifica se a letra está na palavra
    def verifica_letra(self, letra):
        self.letra = letra

        if letra in self.palavra and letra not in self.listaCorretas:
            self.listaCorretas.append(letra)
        elif letra not in self.palavra and letra not in self.listaErradas:
            self.listaErradas.append(letra)
        else:
            return False

        return True

    def fim_jogo(self):
        return self.vencedor() or (len(self.listaErradas) == 6)

    def vencedor(self):
        if '_' not in self.esconde_palavra():
            return True
        return False

    def esconde_palavra(self):
        oculto = ''
        for letra in self.palavra:
            if letra not in self.listaCorretas:
                oculto += '_'
            else:
                oculto += letra
        return oculto

    def imprime_status(self):
        print(tabuleiro[len(self.listaErradas)])
        print("\nPalavra: " + self.esconde_palavra())
        print("\nLetras erradas: ",)
        for letra in self.listaErradas:
            print(letra,)
        print()
        print("Letras corretas: ",)
        for letra in self.listaCorretas:
            print(letra,)
        print()


def escolhe_palavra():
    with open("palavras.txt", "rt") as f:
        lista = f.readlines()
    return lista[random.randint(0, len(lista))].strip()

def main():

    jogo = Forca(escolhe_palavra())

    while not jogo.fim_jogo():
        jogo.imprime_status()
        user_input = input("\nDigite uma letra: ")
        jogo.verifica_letra(user_input)

    jogo.imprime_status()

    if jogo.vencedor():
        print("Parabéns você venceu!!")
    else:
        print("Você perdeu!!")
        print("A palavra correta era: {}".format(jogo.palavra))

if __name__ == "__main__":
    main()