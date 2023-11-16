"""
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetA = []
soma = 0
for i in range(10):
    num = int(input(f"{i}. Insira um número: "))
    vect.append(num)

for i in range(len(vetA)):
    soma += vetA[i]**2
print(f"A soma dos quadrados dos elementos do vetor é de {soma}")