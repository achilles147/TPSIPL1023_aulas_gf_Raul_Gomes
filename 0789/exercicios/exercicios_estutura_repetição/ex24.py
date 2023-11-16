"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
"""
N = int(input("Quantas avaliações vai introduzir? "))

soma = 0
media = 0

for i in range(N):
    ava = int(input("Avaliação: "))
    soma = soma + ava
    media = soma / N
print(f"A média é de {media:.0f} valores.")
"""
print("""
(Inserir numero negativo para parar cálculo)
""")
nota = float(input("Avaliação: "))
soma = 0
n_notas = 0

while (nota >= 0):
    n_notas += 1
    soma = soma + nota
    nota = float(input("Avaliação: "))

media = soma / n_notas
print(f"A média é de {media:.1f}")






