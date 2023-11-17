"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
def classificacão():
    if sim < 2:
        culpa = "inocente"
    elif sim == 2:
        culpa = "suspeita"
    elif sim < 5:
        culpa = "cúmplice"
    else:
        culpa = "assassíno"
    print(f"\nA pessoa é classificada como {culpa}")

perguntas = ["Telefonou para a vítima",
             "Esteve no local do crime",
             "Mora perto da vítima",
             "Devia dinheiro para a vítima",
             "Já trabalhou com a vítima"]
sim = 0
for i in range(len(perguntas)):
    resp = input(f"{perguntas[i]} (s/n) ?")
    while resp.lower() != "s" and resp.lower() != "n":
        print("Resposta ínválida... tente denovo\n")
        resp = input(f"{perguntas[i]} (s/n) ?")
    if resp.lower() == "s":
        sim += 1
classificacão()
