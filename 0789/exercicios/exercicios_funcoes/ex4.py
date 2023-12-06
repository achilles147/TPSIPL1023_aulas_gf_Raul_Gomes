"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def num(n):
    if n > 0:
        print('P')
    elif n <= 0:
        print('N')

num(4)
num(-4)
num(0)