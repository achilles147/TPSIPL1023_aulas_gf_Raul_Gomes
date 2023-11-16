"""
Faça um Programa que leia um vetor de 10
números reais e mostre-os na ordem inversa.
"""

num_list = []
for i in range(10):
    num = float(input("Numero:"))
    num_list.append(num)
num_list.reverse()
print(num_list)