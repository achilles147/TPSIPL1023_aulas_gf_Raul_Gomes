"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de
notas existentes na máquina.


Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

valor_req = int(input("Quanto valor quer levantar?"))

if valor_req > 10 and valor_req < 600: #ex 578
        notas100 = valor_req // 100; # Notas de 100
        resto100 = valor_req % 100; # sobra

        notas50 = resto100 // 50;
        resto50 = resto100 % 50;

        notas10 = resto50 // 10;
        resto10 = resto50 % 10;

        notas5 = resto10 // 5;
        resto5 = resto10 % 5;

        notas1 = resto5 // 1;
        resto1 = resto5 % 1;


print(f"Para levantar {valor_req}, serão necessárias  ")
print(f"Notas de 100: {notas100}")
print(f"Notas de 50: {notas50}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 5: {notas5}")
print(f"Notas de 1: {notas1}")

