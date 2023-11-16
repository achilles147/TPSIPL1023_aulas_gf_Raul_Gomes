"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

fact = int(input("Factorial de: "))
print(f"{fact}! = ", end="")
val = 1

for i in reversed(range(1, fact + 1)):
    val *= i
    if i != 1:
        print(f"{i}", end=" . ")
    else:
        print(f"{i}", end=" = ")
print(val)