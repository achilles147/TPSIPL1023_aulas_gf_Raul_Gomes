"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

# alcool -> ate 20 litros, desconto 3% por litro
#        -> + de 20 litros, desconto 5% por litro -> 1,90 por litro

# gasolina -> ate 20 litros, desconto de 4% por litro
#          -> + de 20 litros, desconto de 6% por litro -> 2,50 por litro



combustivel = input("\nSelecione o tipo de combustivél:\n\n(A) - Álcool\n(G) - Gasolina\n\n")

litros = int(input("\nSelecione a quantidade em litros: \n\n"))

if combustivel == "G":
    tipo_combustivel = "Gasolina"
    if litros <= 20:
         val = (litros * 2.50) - (litros * (0.04 * 2.50))#cálculo do desconto(4%) < 20;
    else:
        val = (litros * 2.50) - (litros * (0.06 * 2.50))#cálculo do desconto(6%) < 20
elif combustivel == "A":
    tipo_combustivel = "Álcool"
    if litros <= 20:
        val = (litros * 1.90) - (litros * (0.03 * 1.90))  # cálculo do desconto(3%) < 20;
    else:
        val = (litros * 1.90) - (litros * (0.05 * 1.90))  # cálculo do desconto(5%) < 20


print(f"\nPela quantidade de litros em {tipo_combustivel} o valor a pagar é de {val:.2f} R$.")