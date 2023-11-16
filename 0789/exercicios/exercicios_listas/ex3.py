"""
Faça um Programa que leia 4 notas,
mostre as notas e a média na tela.
"""

list_notas = []
for i in range(4):
    x = int(input("Nota:"))
    list_notas.append(x)
soma = 0
media = 0
for i in range(len(list_notas)):
    soma += list_notas[i]
media = soma / 4
print(f"A media é de {media}")