"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o
programa permitindo que o usuário digite o salário inicial do funcionário.
"""

salario95 = 1000
percent = 1.5
percentual = 100 / percent
salario96 = salario95 * (percentual + 1)
ano = 1996

while ano != 2023:
    ano+=1
    percent * 2
print(ano)
print(salario96)
print(percent)



