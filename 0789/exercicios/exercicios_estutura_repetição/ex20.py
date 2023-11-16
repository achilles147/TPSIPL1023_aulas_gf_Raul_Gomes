"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""



cont = 's'

while cont == 's':
    num = int(input("Calcule o fatorial: "))
    if num < 16 and num > 0:
        fact = num
        for i in range(1, num):
            fact *= i
        print(f"{num}! =", end=" ")
        for i in reversed(range(1, num + 1)):
            if i != 1:
                print(i, end=".")
            else:
                print(f"{i} = {fact}")
                cont = input("Repetir? (s/n): ")
    else:
        cont = 'n'


