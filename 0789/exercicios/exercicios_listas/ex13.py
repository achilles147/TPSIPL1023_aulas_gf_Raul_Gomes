"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""


meses = ["janeiro",
         "fevereiro",
         "março",
         "abril",
         "maio",
         "junho",
         "julho",
         "agosto",
         "setembro",
         "outubro",
         "novembro",
         "dezembro"]

temp_2023 = {}
for i in range(len(meses)):
    temp = float(input(f"Qual a média do mês de {meses[i]}: "))
    temp_2023[meses[i]] = temp

def mediaMeses():
    soma = 0
    media = 0
    for values in temp_2023.values():
        soma += values
        media = soma / len(meses)
    for i in temp_2023.values():
        if i < media:
            print(f"")
    return media


