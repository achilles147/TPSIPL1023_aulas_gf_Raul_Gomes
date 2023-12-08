"""
Desenha moldura.

Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.

Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.

Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
"""

def moldura(colunas, linhas):
    print("+",end="")
    for i in range(colunas):
        print("-", end="")
    print("+", end="")
    print()
    while linhas != 0:
        print("|", end="")
        for i in range(colunas):
            print(" ", end="")
        print("|")
        linhas -= 1
    print("+", end="")
    for i in range(colunas):
        print("-", end="")
    print("+", end="")


moldura(10,2)

