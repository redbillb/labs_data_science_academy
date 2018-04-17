# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
     |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
+========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.hideword = ''
        self.hide_word()
        self.contadorBoard = 0
        self.acertadas = []
        self.erradas = []

    # Método para esconder a palavra
    def hide_word(self):
        for caracter in self.word:
            self.hideword += "_"

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.erradas) >= 6:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' in self.hideword:
            return False
        else:
            return True

    # Método para verificar se o letra faz parte da palavra
    def guess(self, verifCaracter):
        acertoerro = False
        string = ''
        for indice in (range(len(self.word))):
            if self.hideword[indice] == '_':
                if self.word[indice] == verifCaracter:
                    string += verifCaracter
                    acertoerro = True
                else:
                    string += '_'
            else:
                string += self.hideword[indice]
        if acertoerro:
            self.acertadas.append(verifCaracter)
        else:
            self.contadorBoard += 1
            self.erradas.append(verifCaracter)
        self.hideword = string

    # Método para imprimir o board na tela
    def print_game_board(self):
        os.system('cls')
        print(board[self.contadorBoard])
        print("\nPalavra: %s" % self.hideword)
        print("\nLetras erradas: ")
        for caracter in self.erradas:
            print("%s" % caracter)
        print("\n")
        print("\nLetras corretas:")
        for caracter in self.acertadas:
            print("%s" % caracter)
        print("\n\n")

    # Método para imprimir na tela a situacao final
    def print_status_final(self):
        if self.hangman_over():
            print("Game over! Voce perdeu.")
            print('A palavara era: %s\n' % self.word)

        if self.hangman_won():
            self.print_game_board()
            print('Parabens voce venceu!!\n')

        

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        print(bank, len(bank))
        saida = bank[random.randint(0, len(bank) - 1)].strip()
    return saida

# Função Main - Execução do Programa
def main():
    while True:
        # Objeto
        game = Hangman(rand_word())

        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        while not game.hangman_won():
            game.print_game_board()
        
            if len(game.erradas) >= 6:
                break
            else:
                palpite = input('Digite uma letra: ')

            if game.hangman_over():
                break
            else:
                game.guess(palpite)

        game.print_status_final()
    
        if (input('Quer jogar de novo (s/n)? ') != 's' ):
            print('\nFoi bom jogar com voce! Agora vá estudar')
            break

# Executa o programa
if __name__ == "__main__":
    main()
