"""
Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""

def piramide(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end="  ")
        print("\n")

n = int(input("n: "))
piramide(n)