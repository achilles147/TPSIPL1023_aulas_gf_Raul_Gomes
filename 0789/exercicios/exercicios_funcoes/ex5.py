"""
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.

A função “altera” o valor de custo para incluir o imposto sobre vendas.

"""


def somaImposto(a,b):
    taxaImposto = a / 100 + 1
    custo = b
    custo_produto = custo * taxaImposto
    print(custo_produto)

somaImposto(10,10)