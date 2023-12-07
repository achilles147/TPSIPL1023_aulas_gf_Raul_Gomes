"""
Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

def reverse(num):
    temp = 0
    while num > 0:
        number = num % 10
        temp = (temp * 10) + number
        num = num // 10
    print(temp)


num = int(input("Numero: "))
reverse(num)

