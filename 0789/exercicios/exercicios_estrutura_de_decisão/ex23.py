"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""



num = float(input("Introduza um numero: "))


if (num == round(num)): #
    if (num % round(num) == 0):
        print("É inteiro.")
    else:
        print("É decimal.")
else:
    print("É decimal.")




