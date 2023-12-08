"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

def divida(valor):
    juros1 = 0
    juros2 = 0.1
    juros3 = 0.15
    juros4 = 0.20
    juros5 = 0.25
    valor_juros1 = valor * juros1
    valor_juros2 = valor * juros2
    valor_juros3 = valor * juros3
    valor_juros4 = valor * juros4
    valor_juros5 = valor * juros5
    valor_parcela1 = (valor + valor_juros1) / 1
    valor_parcela2 = (valor + valor_juros2) / 3
    valor_parcela3 = (valor + valor_juros3) / 6
    valor_parcela4 = (valor + valor_juros4) / 9
    valor_parcela5 = (valor + valor_juros5) / 12

    print(f"""
    Valor da Dívida     Valor dos Juros     Quantidade de Parcelas      Valor da Parcela
    R$ {valor}              {valor_juros1}                  1                           {valor_parcela1:.2f}
    R$ {valor}              {valor_juros2}              3                           {valor_parcela2:.2f}
    R$ {valor}              {valor_juros3}              6                           {valor_parcela3:.2f}
    R$ {valor}              {valor_juros4}              9                           {valor_parcela4:.2f}
    R$ {valor}              {valor_juros5}              12                          {valor_parcela5:.2f}
    
    """)

print(divida(1000))


