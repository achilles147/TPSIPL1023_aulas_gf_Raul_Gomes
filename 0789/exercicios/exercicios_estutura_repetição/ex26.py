"""Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""


n_eleitores = int(input("Quantos eleitores são? "))

cand1 = 0
cand2 = 0
cand3 = 0

for i in range(n_eleitores):
    print("\nCandidato 1?\nCandidato 2?\nCandidato 3?")
    voto = int(input("Vota em que candidato? "))
    match voto:
        case 1:
            cand1 += 1
            print("Obrigado pelo seu voto")
        case 2:
            cand2 += 1
            print("Obrigado pelo seu voto")
        case 3:
            cand3 += 1
            print("Obrigado pelo seu voto")
        case default:
            print("Erro")

percentagem1 = 100 * cand1 / n_eleitores
percentagem2 = 100 * cand2 / n_eleitores
percentagem3 = 100 * cand3 / n_eleitores

print(f"\nO Candidato 1 teve {cand1} votos. {percentagem1:.1f}% dos votos")
print(f"O Candidato 2 teve {cand2} votos. {percentagem2:.1f}% dos votos")
print(f"O Candidato 3 teve {cand3} votos. {percentagem3:.1f}% dos votos")
