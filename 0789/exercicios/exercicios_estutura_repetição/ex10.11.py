"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))


if num2 < num1:
    x = num1
    num1 = num2
    num2 = x
soma = 0
for i in range(num1 + 1, num2):
    print(i, end=" + ")
    soma += i

print(f"= {soma}")