def reset():
    jogo[0][0] = '_'
    jogo[1][0] = '_'
    jogo[2][0] = '_'
    jogo[0][1] = '_'
    jogo[1][1] = '_'
    jogo[2][1] = '_'
    jogo[0][2] = '_'
    jogo[1][2] = '_'
    jogo[2][2] = '_'


def check_score():
    if ((jogo[0][0] == 'x' and jogo[0][1] == 'x' and jogo[0][2] == 'x') or
            (jogo[0][0] == 'x' and jogo[1][0] == 'x' and jogo[2][0] == 'x') or
            (jogo[0][0] == 'x' and jogo[1][1] == 'x' and jogo[2][2] == 'x') or
            (jogo[2][0] == 'x' and jogo[2][1] == 'x' and jogo[2][2] == 'x') or
            (jogo[2][0] == 'x' and jogo[1][1] == 'x' and jogo[0][2] == 'x') or
            (jogo[0][2] == 'x' and jogo[1][2] == 'x' and jogo[2][2] == 'x') or
            (jogo[0][1] == 'x' and jogo[1][1] == 'x' and jogo[2][1] == 'x') or
            (jogo[1][0] == 'x' and jogo[1][1] == 'x' and jogo[1][2] == 'x') or
            (jogo[0][0] == 'o' and jogo[0][1] == 'o' and jogo[0][2] == 'o') or
            (jogo[0][0] == 'o' and jogo[1][0] == 'o' and jogo[2][0] == 'o') or
            (jogo[0][0] == 'o' and jogo[1][1] == 'o' and jogo[2][2] == 'o') or
            (jogo[2][0] == 'o' and jogo[2][1] == 'o' and jogo[2][2] == 'o') or
            (jogo[2][0] == 'o' and jogo[1][1] == 'o' and jogo[0][2] == 'o') or
            (jogo[0][2] == 'o' and jogo[1][2] == 'o' and jogo[2][2] == 'o') or
            (jogo[0][1] == 'o' and jogo[1][1] == 'o' and jogo[2][1] == 'o') or
            (jogo[1][0] == 'o' and jogo[1][1] == 'o' and jogo[1][2] == 'o')):
        board()
        return endgame()
    else:
        return 1


def endgame():
    resp = input(f"Ganhou {user}! Queres jogar denovo (s/n)? ")
    while resp != "s" and resp != "n":
        print("Erro. ")
        resp = input(f"Ganhou {user}! Queres jogar denovo (s/n)? ")
    if resp == 's':
        reset()
        return 1
    elif resp == 'n':
        print("Até à proxima!")
        return 2


def validacao_input(var):
    while True:
        try:
            user_input = int(input(var))
            if user_input > 3 or user_input < 1:
                print("Coordenada não encontrada. Tenta denovo.")
                continue
            return user_input
        except ValueError:
            print("Erro. Tenta denovo.")

jogo = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]


def board():
    print(f"""
    {"-"*26+"\n"}
           1   2   3    x
        1  {jogo[0][0]}   {jogo[1][0]}   {jogo[2][0]}
        2  {jogo[0][1]}   {jogo[1][1]}   {jogo[2][1]}
        3  {jogo[0][2]}   {jogo[1][2]}   {jogo[2][2]}
        
        y
        """)


jogadorx = []
jogadory = []

print("\n" + "=" * 15 + "Jogo do Galo" + "=" * 15)
turn = 0
game = 1
while game == 1:
    board()
    if turn == 0:
        if turn == 0:
            user = 'X'
        else:
            user = 'O'
        print(f"\nSão os {user}'s a jogar")
        jogadax = validacao_input("Coordenada X: ")
        jogaday = validacao_input("Coordenada Y: ")
        while jogo[jogadax - 1][jogaday - 1] == 'x' or jogo[jogadax - 1][jogaday - 1] == 'o':
            print("Coordenada ocupada. Tenta denovo.")
            jogadax = validacao_input("Coordenada X: ")
            jogaday = validacao_input("Coordenada Y: ")
        jogo[jogadax - 1][jogaday - 1] = 'x'
        turn = 1
    elif turn == 1:
        if turn == 0:
            user = 'X'
        else:
            user = 'O'
        print(f"\nSão os {user}'s a jogar")
        jogadax = validacao_input("Coordenada X: ")
        jogaday = validacao_input("Coordenada Y: ")
        while jogo[jogadax - 1][jogaday - 1] == 'x' or jogo[jogadax - 1][jogaday - 1] == 'o':
            print("Coordenada ocupada. Tenta denovo.")
            jogadax = validacao_input("Coordenada X: ")
            jogaday = validacao_input("Coordenada Y: ")
        jogo[jogadax - 1][jogaday - 1] = 'o'
        turn = 0
    game = check_score()