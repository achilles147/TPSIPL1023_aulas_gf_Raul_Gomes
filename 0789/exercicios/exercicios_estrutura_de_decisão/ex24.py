"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;

positivo ou negativo;

inteiro ou decimal.
"""

print("1. Par ou Ímpar")
print("2. Positivo ou Negativo")
print("3. Inteiro ou Decimal")

operacao = int(input("\nInsira o numero da operação que deseja realizar: 1 / 2 / 3  "))



if (operacao == 1):
    num1 = int(input("Insira um numero a analisar: "))
    if (num1 % 2 == 0):
        print("O seu número é par.")
    else:
        print("O seu número é impar.")
elif (operacao == 2):
    num1 = int(input("Insira um numero a analisar: "))
    if (num1 > 0):
        print("O seu número é positivo.")
    else:
        print("O seu número é negativo.")
elif (operacao == 3):
    num1 = float(input("Insira um numero a analisar: "))
    if (num1 == round(num1)):  #
        if (num1 % round(num1) == 0):
            print("O seu número é inteiro.")
        else:
            print("O seu número é decimal.")
    else:
        print("O seu número é decimal.")
else:
    print("Operação desconhecida.")

