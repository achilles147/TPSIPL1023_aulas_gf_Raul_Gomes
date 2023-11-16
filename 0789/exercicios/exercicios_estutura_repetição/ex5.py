"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""



pais_A = int(input("Numero de habitantes A inicias: "))
percentagem_A = float(input("Taxa de crescimento A: "))
pais_B = int(input("Numero de habitantes B inicias: "))
percentagem_B = float(input("Taxa de crescimento B: "))

taxa_A = percentagem_A / 100 + 1
taxa_B = percentagem_B / 100 + 1
anos = 0

while pais_A < pais_B:
    anos += 1
    pais_A *= taxa_A
    pais_B *= taxa_B

print(f"\nSerão preciso {anos} para o país A ter {pais_A:.0f} habitantos e o país B {pais_B:.0f} habitantes.")

