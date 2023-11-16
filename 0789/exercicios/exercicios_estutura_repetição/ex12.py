"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
"""

num1 = int(input("Insira o número: "))

print(f"\nTabuada do {num1}:")
for i in range(1,11):
    resp = num1 * i
    print(f"{num1} x {i} = {resp}")