"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

notas = []

for i in range(10):
    x = float(input("Nota: "))
    notas.append(x)
for i in range(len(notas)):
    if notas[i] > 7.0:
        print(notas[i], end=" ")