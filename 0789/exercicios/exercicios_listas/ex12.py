"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com
mais de 13 anos possuem altura inferior à média de
altura desses alunos.
"""


stats = {}
soma = 0
media = 0
infmedia = 0
for i in range(5):
    idade = int(input("Idade: "))
    altura = int(input("Altura: "))
    stats[idade] = altura

print(stats)

for elm in stats.values():
    soma += elm
media = soma / len(stats)
print(media)

for i in stats.keys():
    if i > 13:
       if stats[i] < media:
           infmedia += 1
print("*" * 45)
print(f"\nHouve {infmedia} com idade superior a 13 e altura inferior à média, que é {media}")