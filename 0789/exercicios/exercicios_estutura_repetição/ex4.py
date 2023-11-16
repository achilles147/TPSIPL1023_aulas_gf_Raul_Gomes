"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a
população do país B, mantidas as taxas de crescimento.
"""

pais_A = 80000
pais_B = 200000
anos = 0
taxa_A = 3 / 100 + 1
taxa_B = 1.5 / 100 + 1

while pais_A < pais_B:
    anos += 1
    pais_A *= taxa_A
    pais_B *= taxa_B

print(f"\nSerão preciso {anos} para o país A ter {pais_A:.0f} habitantos e o país B {pais_B:.0f} habitantes.")

