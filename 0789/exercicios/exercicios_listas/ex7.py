"""
Faça um Programa que leia um vetor de 5 números inteiros,
mostre a soma, a multiplicação e os números.
"""

num_list = []
soma = 0
multiplicacao = 1

for i in range(5):
    x = int(input("Num: "))
    num_list.append(x)
    soma += x

for i in range(len(num_list)):
    multiplicacao *= num_list[i]

print(f"Numeros: {num_list}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")