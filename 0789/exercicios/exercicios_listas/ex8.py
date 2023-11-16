"""
Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor. Imprima a
idade e a altura na ordem inversa a ordem lida.
"""

idade = []
altura = []

for i in range(5):
    x = int(input("Idade: "))
    y = int(input("Altura: "))
    idade.append(x)
    altura.append(y)

idade.reverse()
altura.reverse()
print(idade)
print(altura)