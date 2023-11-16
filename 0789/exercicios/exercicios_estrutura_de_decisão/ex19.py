"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = input("Insira um número inteiro menor que 1000: ")

if int(num) < 1000 and int(num) > 99:
    if int(num[0]) == 1:
        centenas = "centena"
    else:
        centenas = "centenas"
    if int(num[1]) == 1:
        dezenas = "dezena"
    else:
        dezenas = "dezenas"
    if int(num[2]) == 1:
        unidades = "unidade"
    else:
        unidades = "unidades"
    print(f"{int(num[0])}{int(num[1])}{int(num[2])} = {num[0]} {centenas},{num[1]} {dezenas} e {num[2]} {unidades}.")
else:
    if int(num[0]) == 1:
        dezenas = "dezena"
    else:
        dezenas = "dezenas"
    if int(num[1]) == 1:
        unidades = "unidade"
    else:
        unidades = "unidades"
    print(f"{int(num[0])}{int(num[1])} = {num[0]} {dezenas} e {num[1]} {unidades}.")
