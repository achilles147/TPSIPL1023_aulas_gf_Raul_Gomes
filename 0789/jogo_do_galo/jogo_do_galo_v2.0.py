
def makeboard(): #cria a board
    n_board = int(input("N-elementos: "))
    for i in range(n_board):
        linha = []
        for j in range(n_board):
            linha.append('_')
        board.append(linha)
def showboard(): #print da board
    print(f"\nRonda {ronda:.0f}\nJogador {jogadores[jogador]}\n"+"-"*20)
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end="\t\t")
        print("\n")

def validacao_input(var): #valida a input caso não seja int e > ou < que o tamanho da board
    while True:
        try:
            user_input = int(input(var))
            if user_input > len(board) or user_input < 1:
                print("Coordenada não encontrada. Tenta denovo.")
                continue
            return user_input
        except ValueError:
            print("Erro. Tenta denovo.")


def reset(): #reset aos valores da board
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = '_'

def checkscore(board, jogadores): #verificar se há combinação vencedora
    for i in range(len(board)):
        if all(cell == jogadores for cell in board[i]) or all(board[j][i] == jogadores for j in range(len(board))):
            #all() retorna True caso os parametros sejam True
            #primeio all() verifica cada linha da board, segundo all() verifica cada coluna
            #cell itera sobre os valores de jogadores['X' ou 'O'] -> ex.: se
            return True
    if all(board[i][i] == jogadores for i in range(len(board))) or all(board[i][len(board) - 1 - i] == jogadores for i in range(len(board))):
        return True
    return False

board = []
jogadores = ['X','O']
ronda = 1
roundc = 0
makeboard()
jogador = 0
print(f"""
{"="*5+"Jogo do Galo"+"="*5}
    """)
while True:
    showboard()
    jogadax = validacao_input("Coordenada X: ")
    jogaday = validacao_input("Coordenada Y: ")
    while board[jogaday - 1][jogadax - 1] == 'X' or board[jogaday - 1][jogadax - 1] == 'O':
        print("Coordenada ocupada. Tenta denovo.")
        jogadax = validacao_input("Coordenada X: ")
        jogaday = validacao_input("Coordenada Y: ")
    board[jogaday-1][jogadax-1] = jogadores[jogador]
    if checkscore(board, jogadores[jogador]):
        showboard()
        resp = input(f"Jogador {jogadores[jogador]} ganhou!\n Repetir (s/n)? ")
        if resp == 'n':
            print("\nObrigado por jogares")
            break
        else:
            reset()
            ronda = 1
            roundc = 0
            continue
    jogador = (jogador + 1) % 2
    if roundc == 1:
        ronda += 1
        roundc = 0
    else:
        roundc += 1
    print(board)