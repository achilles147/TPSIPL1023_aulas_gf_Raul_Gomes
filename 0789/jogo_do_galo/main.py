


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


jogo = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

print("\n"+"="*15+"Jogo do Galo"+"="*15)

turn = 0
jogadorx = []
jogadory = []

while True:
    print(f"""
    
       1   2   3    x
    1  {jogo[0][0]}   {jogo[1][0]}   {jogo[2][0]}
    2  {jogo[0][1]}   {jogo[1][1]}   {jogo[2][1]}
    3  {jogo[0][2]}   {jogo[1][2]}   {jogo[2][2]}
    
    y
    """)

    if jogo[0][0] == 'x':
        if jogo[0][1] == 'x':
            if jogo[0][2] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != "s" and resp != "n":
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
        elif jogo[1][0] == 'x':
            if jogo[2][0] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
        elif jogo[1][1] == 'x':
            if jogo[2][2] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[2][0] == 'x':
        if jogo[2][1] == 'x':
            if jogo[2][2] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
        if jogo[1][1] == 'x':
            if jogo[0][2] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[0][2] == 'x':
        if jogo[1][2] == 'x':
            if jogo[2][2] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                    while resp != 's' and resp != 'n':
                        print("Erro. ")
                        resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                    if resp == 's':
                        reset()
                        continue
                    elif resp == 'n':
                        print("Até à proxima!")
                        break
    elif jogo[0][1] == 'x':
        if jogo[1][1] == 'x':
            if jogo[2][1] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[1][0] == 'x':
        if jogo[1][1] == 'x':
            if jogo[1][2] == 'x':
                resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break

    if jogo[0][0] == 'o':
        if jogo[0][1] == 'o':
            if jogo[0][2] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
        elif jogo[1][0] == 'o':
            if jogo[2][0] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
        elif jogo[1][1] == 'o':
            if jogo[2][2] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[2][0] == 'o':
        if jogo[2][1] == 'o':
            if jogo[2][2] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != "s" and resp != "n":
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
        if jogo[1][1] == 'o':
            if jogo[0][2] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[0][2] == 'o':
        if jogo[1][2] == 'o':
            if jogo[2][2] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[0][1] == 'o':
        if jogo[1][1] == 'o':
            if jogo[2][1] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break
    elif jogo[1][0] == 'o':
        if jogo[1][1] == 'o':
            if jogo[1][2] == 'o':
                resp = input("Ganhou Y! Queres jogar denovo (s/n)? ")
                while resp != 's' and resp != 'n':
                    print("Erro. ")
                    resp = input("Ganhou X! Queres jogar denovo (s/n)? ")
                if resp == 's':
                    reset()
                    continue
                elif resp == 'n':
                    print("Até à proxima!")
                    break

    if turn == 0:
        print("\nSão os X's a jogar")
        jogadax = int(input("Coordenada x: "))
        jogaday = int(input("Coordenada y: "))
        while jogo[jogadax-1][jogaday-1] == 'x' or jogo[jogadax-1][jogaday-1] == 'o':
            print("Coordenada ocupada. Tenta denovo.")
            jogadax = int(input("Coordenada x: "))
            jogaday = int(input("Coordenada y: "))
        jogo[jogadax-1][jogaday-1] = 'x'
        turn = 1
    elif turn == 1:
        print("\nSão os O's a jogar")
        jogadax = int(input("Coordenada x: "))
        jogaday = int(input("Coordenada y: "))
        while jogo[jogadax-1][jogaday-1] == 'x' or jogo[jogadax-1][jogaday-1] == 'o':
            print("Coordenada ocupada. Tenta denovo.")
            jogadax = int(input("Coordenada x: "))
            jogaday = int(input("Coordenada y: "))
        jogo[jogadax - 1][jogaday - 1] = 'o'
        turn = 0







