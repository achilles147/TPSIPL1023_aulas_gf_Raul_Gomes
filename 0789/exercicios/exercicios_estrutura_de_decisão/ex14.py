"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao
longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
"""

num1 = float(input("Insira a primeira nota: "))
num2 = float(input("Insira a segunda nota: "))

media = (num1 + num2) / 2

print("Média de Aproveitamento")

if media <= 10 and media >= 9:
    conceito = "A"
elif media < 9 and media >= 7.5:
    conceito = "B"
elif media < 7.5 and media >= 6:
    conceito = "C"
elif media < 6 and media >= 4:
    conceito = "D"
elif media < 4 and media >= 0:
    conceito = "E"
else:
    print("Erro na média.")

if conceito == "A" or conceito == "B" or conceito == "C":
    aprovacao = "Aprovado"
elif conceito == "D" or conceito == "E":
    aprovacao = "Reprovado"



print(f"A média é de {media} valores. Está {aprovacao}, com a nota {conceito}.")