"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
alto e o número do aluno mais baixo, junto com suas alturas.
"""
altura_menor = 250
altura_maior = 100
maior = 0
menor = 0
aluno_maior = 0
aluno_menor = 0

for i in range(10):
    aluno_num = int(input("Número do aluno: "))
    aluno_altura = int(input("Altura do aluno (cm): "))
    if aluno_altura > altura_maior:
        altura_maior = aluno_altura
        aluno_maior = aluno_num
    elif aluno_altura < altura_menor:
        altura_menor = aluno_altura
        aluno_menor = aluno_num
print(f"\nNumero do aluno maior: {aluno_maior}")
print(f"Numero do aluno menor: {aluno_menor}")