"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""


num = int(input("Insira um número entre 0 e 10:"))

while num < 0 or num > 10:
    print("Número inválido.")
    num = int(input("Insira um número entre 0 e 10:"))
print("Ótimo número!")
