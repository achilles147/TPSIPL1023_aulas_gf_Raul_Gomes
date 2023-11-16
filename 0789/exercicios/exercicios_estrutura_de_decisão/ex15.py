"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for
maior que o terceiro;

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input("Comprimento do lado 1: "))
lado2 = float(input("Comprimento do lado 2: "))
lado3 = float(input("Comprimento do lado 3: "))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print("Triangulo é válido")

    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print("É um triângulo equilátero.")
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 != lado2 and lado1 == lado3) or (
            lado2 == lado3 and lado1 != lado3):
        print("É um triângulo isósceles")
    elif lado1 != lado2 and lado1 != lado3:
        print("É um triângulo escaleno")
else:
    print("Triangulo inválido.")



