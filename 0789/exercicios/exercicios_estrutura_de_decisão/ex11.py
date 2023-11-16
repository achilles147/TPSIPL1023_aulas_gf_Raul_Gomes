"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario_atual = float(input("Insira o seu salário: "))

if salario_atual <= 280:
    aumento_percentual = 20
    valor_percentual = salario_atual * 0.20
    salario_atualizado = salario_atual * 1.20
elif salario_atual <= 700 and salario_atual > 280:
    aumento_percentual = 15
    valor_percentual = salario_atual * 0.15
    salario_atualizado = salario_atual * 1.15
elif salario_atual <= 1500 and salario_atual > 700:
    aumento_percentual = 10
    valor_percentual = salario_atual * 0.1
    salario_atualizado = salario_atual * 1.1
elif salario_atual > 1500:
    aumento_percentual = 5
    valor_percentual = salario_atual * 0.05
    salario_atualizado = salario_atual * 1.05
else:
    print("Valor negativo.")

print(f"O seu salário atual é: \nSalário -> {salario_atual}")
print(f"Aplica-se um aumento de {int(aumento_percentual)}%.")
print(f"O valor de aumento é {valor_percentual:.2f} R%.")
print(f"O salário atualizado é cerca de {salario_atualizado:.2f} R%.")