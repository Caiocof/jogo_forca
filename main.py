# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from hangman import Hangman


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("frases.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    accert = ''
    error = ''
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        print(f'Palavra: {game.getFrase()}')
        print(f'Letras erradas: {error}')
        print(f'Letras certas: {accert}')
        print(f'Você ainda tem {6 - game.getRound()} chances')

        letter = input('Digite uma letra: ')

        if game.guess(letter):
            accert += f'{letter} '
        else:
            error += f'{letter} '

    # Verifica o status do jogo
    # game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print(f'A palavra era "{game.word.upper()}"')

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()