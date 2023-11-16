"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a
quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

esc = int(input("\nO que pretende comprar?\n(Selecione o número correspondente)\n\t1. Morango\n\t2. Maçã\n3. Fim de compra\n"))

quilos_morango = 0
quilos_maca = 0

if esc == 1 or esc == 2 or esc == 3:
    while esc != 3:
        if esc == 1:
            quilos_morango = float(input("Quantos quilos de morango quer comprar?\n"))
            esc = int(input("\nO que pretende comprar?\n(Selecione o número correspondente)\n\t1. Morango\n\t2. Maçã\n3. Fim de compra\n"))
        elif esc == 2:
            quilos_maca = float(input("Quantos quilos de maça quer comprar?\n"))
            esc = int(input("\nO que pretende comprar?\n(Selecione o número correspondente)\n\t1. Morango\n\t2. Maçã\n3. Fim de compra\n"))

    if quilos_morango <= 5:
        val_morango = quilos_morango * 2.5
    else:
        val_morango = quilos_morango * 2.2

    if quilos_maca <= 5:
        val_maca = quilos_maca * 1.8
    else:
        val_maca = quilos_maca * 1.5

    val_total_morango = val_morango * quilos_morango
    val_total_maca = val_maca * quilos_maca

    quilos_total = quilos_morango + quilos_maca
    val_total = val_total_morango + val_total_maca

    if quilos_total > 8 or val_total > 25:
        val_total_desc = val_total * 0.9
        print(f"Valor com desconto (+8kg ou +25 R$: {val_total_desc:.2f} R$.\nSem desconto (10%): {val_total:.2f} R$.")
    print(f"O valor total é de:\n\tQuatidade morango (kg): {quilos_morango} -> {val_morango:.2f} R$\n\tQuantidade maçã (kg): {quilos_maca} -> {val_maca:.2f} R$\n\tQuantidade total: {quilos_total} Kgs.")
else:
    print("\n\nErro")


