"""Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))
potencia = 1
val = base

while potencia != expoente:
    val *= base
    potencia += 1

print(f"O valor é {val}")