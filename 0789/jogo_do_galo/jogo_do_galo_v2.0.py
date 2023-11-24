#criar board n-elementos
def board():
    n_board = int(input("n: "))
    board = []
    for i in range(n_board):
        linha = []
        for j in range(n_board):
            linha.append('_')
        board.append(linha)
    print(board)
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end="\t")
        print("\n")

board()