"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""


num_par = 0
num_impar = 0

for i in range(10):
    num = int(input("Insira um número: "))

    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1
print(f"Existem {num_par} numeros pares e {num_impar} numeros impares.")

