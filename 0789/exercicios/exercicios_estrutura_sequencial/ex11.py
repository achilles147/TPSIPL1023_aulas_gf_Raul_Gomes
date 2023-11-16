"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

inteiro1 = int(input("Introduza um numero inteiro: "))
inteiro2 = int(input("Introduza um outro numero inteiro: "))
real1 = float(input("Introduza um numero real: "))

print("\"o produto do dobro do primeiro com metade do segundo\":", inteiro1 * (inteiro2/2))
print("\"a soma do triplo do primeiro com o terceiro\":", (3 * inteiro1) + real1)
print("\"o terceiro elevado ao cubo\":", real1**3)
