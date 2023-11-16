"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

num = int(input("Insira um numero: "))
primo = False

for i in range(2, num):
    if (num % i) == 0:
        primo = True
        break
if primo:
    print("não é primo")
else:
    print("é primo")
