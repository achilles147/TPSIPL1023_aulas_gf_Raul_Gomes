"""
Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.

O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470.

Escreva um programa (usando um array de contadores) que determine
quantos vendedores receberam salários nos seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""


vendas = []
salarios = []
print("-"*19, "Vendas semanais", "-"*18,
      "\nPremir 'ENTER' sem valor para parar inserção de vendas\n",
      "-"*52)

while True:
    try:
        num = float(input("Insira vendas semanais: "))
        vendas.append(num)
    except ValueError:
        break
for i in range(len(vendas)):
    salario = vendas[i] * 0.09
    salarios.append(salario)

escaloes = ([*range(200,300)],
            [*range(300,400)],
            [*range(400,500)],
            [*range(500,600)],
            [*range(600,700)],
            [*range(700,800)],
            [*range(800,900)],
            [*range(900,1000)])

contador = [0,0,0,0,0,0,0,0,0]

for i in range(len(salarios)):
    if salarios[i] > 1000:
        contador[8] += 1
    else:
        for j in range(len(escaloes)):
            if salarios[i] in escaloes[j]:
                contador[j] += 1
print(f"""
200-299: {contador[0]}
300-399: {contador[1]}
400-499: {contador[2]}
500-599: {contador[3]}
600-699: {contador[4]}
700-799: {contador[5]}
800-899: {contador[6]}
900-999: {contador[7]}
>= 1000: {contador[8]}
""")
