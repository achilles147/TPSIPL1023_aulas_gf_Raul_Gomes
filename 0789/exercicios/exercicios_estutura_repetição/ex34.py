"""
Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia.

Um número primo é aquele
que é divisível apenas por um e por ele mesmo.

Faça um programa que peça um número inteiro e
determine se ele é ou não um número primo.

"""

num = int(input("Insira um número: "))
primo = False


for i in range(2, num):
    if (num % i == 0):
        primo = True
        print(i)
if primo:
    print(f"Não é primo")
else:
    print("É primo")







