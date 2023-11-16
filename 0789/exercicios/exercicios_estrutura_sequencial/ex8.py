#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

preco_hora = int(input("Introduza o valor por hora: "))
qte_hora = int(input("Introduza o número de horas mensais: "))

valor_total = qte_hora * preco_hora

print(f"O salário deste mês é de {valor_total}.")
