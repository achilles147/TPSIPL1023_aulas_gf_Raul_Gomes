"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é
descontado (é a empresa que deposita). O Salário Líquido corresponde ao
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o
valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

val_hora = float(input("Qual é o seu valor por hora? "))
qte_hora = float(input("Quantas horas trabalhadas mensalmente? "))
salario_bruto = qte_hora * val_hora
salario_bruto_ir = salario_bruto * 0.05
salario_bruto_inss = salario_bruto * 0.10
salario_bruto_fgts = salario_bruto * 0.11
descontos = salario_bruto_ir + salario_bruto_inss
salario_liquido = salario_bruto - descontos


print(f"Salário Bruto: ({val_hora} * {qte_hora})        : R$ {salario_bruto:.2f}")
print(f"(-) IR (5%)     : R$ {salario_bruto_ir:.2f}")
print(f"(-) INSS (10%)     : R$ {salario_bruto_inss:.2f}")
print(f"FGTS (11%)     : R$ {salario_bruto_fgts:.2f}")
print(f"Total de descontos     : R$ {descontos:.2f}")
print(f"Salário Liquido     : R$ {salario_liquido:.2f}")