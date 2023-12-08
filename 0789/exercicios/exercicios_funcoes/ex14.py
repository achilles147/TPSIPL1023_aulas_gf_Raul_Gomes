"""
Quadrado mágico.

Um quadrado mágico é aquele dividido em linhas e colunas,
com um número em cada posição e no qual a soma das linhas,
colunas e diagonais é a mesma.

Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
com as características acima. Dica: produza todas as combinações possíveis e
verifique a soma quando completar cada quadrado.

Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""
import random


def shuffle(list):
    random.shuffle(list)
    horizontal1 = list[0] + list[1] + list[2]
    horizontal2 = list[3] + list[4] + list[5]
    horizontal3 = list[6] + list[7] + list[8]
    vertical1 = list[0] + list[3] + list[6]
    vertical2 = list[1] + list[4] + list[7]
    vertical3 = list[2] + list[5] + list[8]
    diagonal1 = list[0] + list[4] + list[8]
    diagonal2 = list[2] + list[4] + list[6]
    if horizontal1 == horizontal2 and horizontal1 == horizontal3 and horizontal1 == vertical1 and horizontal1 == vertical2 and horizontal1 == vertical3 and horizontal1 == diagonal1 and horizontal1 == diagonal2:
        if list in lista_comb:
            print("Current list already added.")
        else:
            print(f"\n{list[0]}\t{list[1]}\t{list[2]}\n{list[3]}\t{list[4]}\t{list[5]}\n{list[6]}\t{list[7]}\t{list[8]}\n")
            lista_comb.append(list.copy())


lista_comb = []
list = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

while len(lista_comb) < 8:
    shuffle(list)
print("=" * 10, "Combinações possíveis", 10 * "=")
for list in lista_comb:
    print(f"\n{list[:3]}\n{list[3:6]}\n{list[6:]}")
