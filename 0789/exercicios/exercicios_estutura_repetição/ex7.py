"""
Faça um programa que leia 5 números e informe o maior número.
"""


"""
maior = 0
for i in range(5):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
print(f"O maior número é {maior}.")
"""

maior = 0
i = 1
while i < 6:
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    i += 1
print(f"O maior número é {maior}.")
