"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = float(input("Insira o valor do produto 1: "))
produto2 = float(input("Insira o valor do produto 2: "))
produto3 = float(input("Insira o valor do produto 3: "))

if produto1 < produto2:
    if produto1 < produto3:
        print("O produto 1 é o mais barato.")
    else:
        print("O produto 3 é o mais batato.")
else:
    if produto2 < produto3:
        print("O produto 2 é o mais barato.")
    else:
        print("O produto 3 é o mais barato.")