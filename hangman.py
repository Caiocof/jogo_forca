from board import BOARD


# Classe
class Hangman:
    # Método Construtor
    rounds = 0
    frase = []

    def __init__(self, word):
        self.word = word

        for i in range(0, len(self.word)):
            self.frase.append('_')

    # Método para adivinhar a letra
    def guess(self, letter):
        i = 0
        if letter in self.word:
            for l in self.word:
                if letter == l:
                    self.frase[i] = letter
                i += 1
            print(BOARD[self.rounds])
            return True
        else:
            self.setRound(1)
            print(BOARD[self.rounds])
            return False

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.rounds >= 6 or self.hangman_won():
            self.setRound(1)
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.getFrase().replace(' ', '') == self.word:
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        pass

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(BOARD[self.rounds])

    def getRound(self):
        return self.rounds

    def setRound(self, new_round):
        self.rounds += new_round

    def getFrase(self):
        return str(self.frase).replace("'", "").replace("[", '').replace(']', '').replace(',', '')
