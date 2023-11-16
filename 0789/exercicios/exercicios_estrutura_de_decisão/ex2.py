# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input("Insira um numero positivo ou negativo: "))

if n > 0:
    print("O seu numero é positivo.")
elif n < 0:
    print("O seu numero é negativo.")
elif n == 0:
    print("O seu numero é igual a zero.")