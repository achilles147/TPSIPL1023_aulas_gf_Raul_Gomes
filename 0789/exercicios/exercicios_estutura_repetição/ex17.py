"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

num = int(input("Calcule o fatorial: "))
fact = num

for i in range(1, num):
    fact *= i

print(f"{num}! =", end=" ")
for i in reversed(range(1, num + 1)):
    if i != 1:
        print(i, end=".")
    else:
        print(f"{i} = {fact}")







