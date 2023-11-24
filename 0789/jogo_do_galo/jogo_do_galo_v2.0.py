#criar board n-elementos

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

def checkscore(board):
    for linha in board:
        if all(value == linha[0] for value in linha):
            return True




board = []
turn = 0
makeboard()
print(f"""
{"="*5+"Jogo do Galo"+"="*5}
    """)
while True:
    showboard()
    if turn == 0:
        print("Jogador X")
        jogadax = int(input("Coordenada x: "))
        jogaday = int(input("Coordenada Y: "))
        board[jogaday-1][jogadax-1] = 'X'
        turn = 1
    elif turn == 1:
        print("Jogador Y")
        jogadax = int(input("Coordenada x: "))
        jogaday = int(input("Coordenada Y: "))
        board[jogaday - 1][jogadax - 1] = 'Y'
        turn = 0
    if checkscore(board):
        print("Linha!")
    else:
        print("perdeu playboi")
    print(board)