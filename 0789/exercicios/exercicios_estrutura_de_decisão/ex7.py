# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("numero 1:"))
num2 = int(input("numero 2:"))
num3 = int(input("numero 3:"))

if num1 > num2:
    if num1 > num3:
        print(f"O maior numero é {num1}")
    else:
        print(f"O maior numero é {num3}")
else:
    if num2 > num3:
        print(f"O maior numero é {num2}")
    else:
        print(f"O maior numero é {num3}")

if num1 < num2:
    if num1 < num3:
        print(f"O menor numero é {num1}")
    else:
        print(f"O menor numero é {num3}")
else:
    if num2 > num3:
        print(f"O menor numero é {num2}")
    else:
        print(f"O menor numero é {num3}")

