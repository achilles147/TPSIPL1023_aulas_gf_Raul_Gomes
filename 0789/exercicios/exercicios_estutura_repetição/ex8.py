"""
Faça um programa que leia 5 números e informe a soma e a média dos números.

"""

i = 1
soma = 0
for i in range(5):
    num = float(input("Insira um numero: "))
    soma += num
    i += 1
media = soma / i
print(f"Esta é a média {media:.2f}")
