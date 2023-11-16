"""Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

n_turmas = int(input("Quantas turmas são? "))
qte_total_alunos = 0

for i in range(n_turmas):
    n_alunos = int(input("Quantos alunos tem esta turma? "))
    if n_alunos > 40:
        print("Esta turma tem demasiados alunos. max 40 alunos")
        n_alunos = int(input("Quantos alunos tem esta turma? "))
    qte_total_alunos += n_alunos

media = qte_total_alunos / n_turmas

print(f"A média de alunos em {n_turmas} turmas é de {media:.1f} alunos.")