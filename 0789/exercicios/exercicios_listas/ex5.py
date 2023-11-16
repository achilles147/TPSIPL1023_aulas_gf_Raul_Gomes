"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
num = []
pares = []
impares = []

for i in range(20):
    x = int(input("Numero: "))
    num.append(x)
    if (x % 2 == 0):
        pares.append(x)
    else:
        impares.append(x)
print(f"Numeros: {num}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
