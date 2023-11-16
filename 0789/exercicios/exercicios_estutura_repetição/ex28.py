"""
Faça um programa que calcule o valor total investido
por um colecionador em sua coleção de CDs e o valor
médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor em cada um.

"""

qte_cd = int(input("Quantos CDs tem? "))
soma = 0
n_cd = 1
for i in range(qte_cd):
    val_cd = float(input(f"Qual o valor do CD {n_cd}? "))
    soma += val_cd
    n_cd += 1

media = soma / qte_cd
print(f"A média de preço de cada CD é de {media:.2f} euros.")
print(f"O valor total do investimento é de {soma} euros.")