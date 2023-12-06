"""
Faça um programa para imprimir:

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
"""

def piramide(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="  ")
        print('\n')

n = int(input("n: "))
piramide(n)