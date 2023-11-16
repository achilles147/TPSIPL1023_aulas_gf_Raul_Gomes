"""
Faça um Programa que leia um vetor de 10
caracteres, e diga quantas
consoantes foram lidas.
Imprima as consoantes.
"""

num_list = []
vogais = 0
consoantes = 0
consoantes_list = []

for i in range(10):
    num = input("Letra: ")
    num_list.append(num)
for i in range(len(num_list)):
    if num_list[i] == 'a' or num_list[i] == 'e' or num_list[i] == 'i' or num_list[i] == 'o' or num_list[i] == 'u':
        vogais += 1
    else:
        consoantes += 1
        consoantes_list.append(num_list[i])
print(consoantes_list)