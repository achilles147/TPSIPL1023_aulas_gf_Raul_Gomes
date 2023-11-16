"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

print("\nResponda a este questionário com (s) de Sim ou (n) de Não:\n")

sim = 0
nao = 0

questao1 = input("Telefonou para a vítima? ")
if questao1 == "s":
    sim = sim + 1;
elif questao1 == "n":
    nao =nao + 1;

questao2 = input("Esteve no local do crime? ")
if questao2 == "s":
    sim = sim + 1;
elif questao2 == "n":
    nao = nao + 1;

questao3 = input("Mora perto da vítima?")
if questao3 == "s":
    sim = sim + 1;
elif questao3 == "n":
    nao = nao + 1;

questao4 = input("Devia algo à vitima? ")
if questao4 == "s":
    sim = sim + 1;
elif questao4 == "n":
    nao = nao + 1;

questao5 = input("Já trabalhou com a vítima? ")
if questao5 == "s":
    sim = sim + 1;
elif questao5 == "n":
    nao = nao + 1;

if (sim <= 2) and (sim > 0):
    print("\nResultado: você é uma suspeita.")
elif (sim > 2) and ( sim < 5):
    print("\nResultado: você é cúmplice.")
elif (sim == 5):
    print("\nResultado: você é o culpado.")
else:
    print("\nResultado: você é inocente.")


