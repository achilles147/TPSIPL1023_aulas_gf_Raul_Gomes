"""
Jogo de Craps.

Faça um programa de implemente um jogo de Craps.

O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
import random


def get_random_num():
    dado1 = random.randrange(1,7)
    dado2 = random.randrange(1,7)
    return dado1 + dado2

def jogada(num):
    temp = num
    if temp == 2 or temp == 3 or temp == 12:
        print(f"Perdeu! O seu resultado foi {temp}, 'craps'")
        return
    elif temp == 7 or temp == 11:
        print(f"Ganhaste! Tiraste um {temp}, 'natural'")
    else:
        print(f"Seu ponto é {temp}")
    while True:
        num1 = get_random_num()
        if num1 == 7:
            print(f"Perdeste... Tiraste um {num1} antes do teu 'ponto'")
            break
        elif num1 == temp:
            print(f"Ganhaste! Saiu o {num1}, o teu ponto!")
            break
        print(f"\nSaiu-te um {num1}, rola outra vez.\n")


jogada(get_random_num())


