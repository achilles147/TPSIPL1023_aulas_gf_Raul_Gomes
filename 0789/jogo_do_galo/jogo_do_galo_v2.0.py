
def makeboard():
    n_board = int(input("N-elementos: "))
    for i in range(n_board):
        linha = []
        for j in range(n_board):
            linha.append('_')
        board.append(linha)
def showboard():
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end="\t\t")
        print("\n")

def validacao_input(var):
    while True:
        try:
            user_input = int(input(var))
            if user_input > len(board) or user_input < 1:
                print("Coordenada não encontrada. Tenta denovo.")
                continue
            return user_input
        except ValueError:
            print("Erro. Tenta denovo.")

def checkscore(board, jogadores):
    for i in range(len(board)):
        if all(cell == jogadores for cell in board[i]) or all(board[j][i] == jogadores for j in range(len(board))):
            return True
    if all(board[i][i] == jogadores for i in range(len(board))) or all(board[i][len(board) - 1 - i] == jogadores for i in range(len(board))):
        return True
    return False

board = []
jogadores = ['X','O']
turn = 0
makeboard()
jogador = 0
print(f"""
{"="*5+"Jogo do Galo"+"="*5}
    """)
while True:
    showboard()
    print(f"Jogador {jogadores[jogador]}")
    jogadax = validacao_input("Coordenada X: ")
    jogaday = validacao_input("Coordenada Y: ")
    board[jogaday-1][jogadax-1] = jogadores[jogador]
    if checkscore(board, jogadores[jogador]):
        showboard()
        print(f"Jogador {jogadores[jogador]} ganhou!")
        break
    jogador = (jogador + 1) % 2
