"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto
de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
"""

valor_hora = float(input("Valor por hora: "))
qte_hora = float(input("Valor por hora: "))

valor_total = qte_hora * valor_hora

print("+ Salário bruto: ", valor_total,"R$")
print("- IR (11%): ", valor_total * 0.11,"R$")
print("- INSS (8%): ", valor_total * 0.08,"R$")
print("- Sindicato (5%): ", valor_total * 0.05,"R$")
print("= Salário líquido : ", valor_total * (1 - (0.11 + 0.08 + 0.05)),"R$")