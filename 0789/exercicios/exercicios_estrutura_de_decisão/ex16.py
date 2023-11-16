"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

# delta = b**2 - 4ac

a = float(input("Valor de 'a':"))


if a == 0:
    print("'a' = 0, a equação não é de segundo grau.")
else:
    b = float(input("Valor de 'b':"))
    c = float(input("Valor de 'c':"))
    if (b**2 - (4*a*c)) < 0:
        print("Delta calculado negativo, a equação não possui raízes reais.")
    elif (b**2 - (4*a*c)) == 0:
        print("Delta igual a zero, a equação possui uma raiz real.")
    elif (b**2 - (4*a*c)) > 0:
        print("Delta calculado positivo, a equação possui duas raizes reais.")

