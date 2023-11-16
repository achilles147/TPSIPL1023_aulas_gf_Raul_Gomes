"""
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a
quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as
informações da compra:

tipo e quantidade de carne,
preço total, tipo de pagamento,
valor do desconto e
valor a pagar.
"""

esc = int(input("\n\t1. File Duplo\n\t2. Alcatra\n\t3. Picanha\nIntroduza o número da Carne a comprar:"))

if esc == 1:
    quilos = float(input("Quantos quilos vai querer? "))
    if quilos <= 5:
        val = quilos * 4.9
    elif quilos > 5:
        val = quilos * 5.8
    esc_pagamento = int(input("\n\t1. Dinheiro\n\t2.Cartão Tabajara (desconto 5%)\nIntroduza o número do seu método de pagamento:"))
    if esc_pagamento == 1:
        print(f"\nDetalhes da sua compra:\n\tTipo de Carne: File Duplo\n\tQuantidade de Carne (kg): {quilos}")
        print(f"\tMétodo de pagamento: Dinheiro\n\tTotal da sua compra: {val} R$")
    elif esc_pagamento == 2:
        desconto = val * 0.05
        val = val * 0.95
        print(f"\nDetalhes da sua compra:\n\tTipo de Carne: File Duplo\n\tQuantidade de Carne (kg): {quilos}")
        print(f"\tMétodo de pagamento: Cartão Tabajara\n\tValor do desconto: {desconto:.2f} R$\n\tTotal da sua compra: {val:.2f} R$")
elif esc == 2:
    quilos = float(input("Quantos quilos vai querer? "))
    if quilos <= 5:
        val = quilos * 5.9
    elif quilos > 5:
        val = quilos * 6.8
    esc_pagamento = int(input("\n\t1. Dinheiro\n\t2. Cartão Tabajara (desconto 5%)\nIntroduza o número do seu método de pagamento:"))
    if esc_pagamento == 1:
        print(f"\nDetalhes da sua compra:\n\tTipo de Carne: Alcatra\n\tQuantidade de Carne (kg): {quilos}")
        print(f"\tMétodo de pagamento: Dinheiro\n\tTotal da sua compra: {val} R$")
    elif esc_pagamento == 2:
        desconto = val * 0.05
        val = val * 0.95
        print(f"\nDetalhes da sua compra:\n\tTipo de Carne: File Duplo\n\tQuantidade de Carne (kg): {quilos}")
        print(f"\tMétodo de pagamento: Cartão Tabajara\n\tValor do desconto: {desconto:.2f} R$\n\tTotal da sua compra: {val:.2f} R$")
elif esc == 3:
    quilos = float(input("Quantos quilos vai querer? "))
    if quilos <= 5:
        val = quilos * 6.9
    elif quilos > 5:
        val = quilos * 7.8
    esc_pagamento = int(input("\n\t1. Dinheiro\n\t2.Cartão Tabajara (desconto 5%)\nIntroduza o número do seu método de pagamento:"))
    if esc_pagamento == 1:
        print(f"\nDetalhes da sua compra:\n\tTipo de Carne: Picanha\n\tQuantidade de Carne (kg): {quilos}")
        print(f"\tMétodo de pagamento: Dinheiro\n\tTotal da sua compra: {val} R$")
    elif esc_pagamento == 2:
        desconto = val * 0.05
        val = val * 0.95
        print(f"\nDetalhes da sua compra:\n\tTipo de Carne: File Duplo\n\tQuantidade de Carne (kg): {quilos}")
        print(f"\tMétodo de pagamento: Cartão Tabajara\n\tValor do desconto: {desconto:.2f} R$\n\tTotal da sua compra: {val:.2f} R$")
else:
    print("Erro na seleção.")



