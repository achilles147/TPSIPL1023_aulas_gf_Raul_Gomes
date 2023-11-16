"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

print("""
===================================
========Introduza um número========
========(entre 0 e 10.000)=========
===================================
""")




continuar = 's'


maior = 0
menor = 10000


while continuar != 'n':
    num = int(input("Numero: "))
    if num > 0 and num < 10000:
        if num > maior:
            maior = num
        else:
            menor = num
        continuar = input("quer continuar (s/n)?")
    else:
        print("Maior que 10000 ou menor que zero.")
        continuar = 'n'


soma = maior + menor
print(f"O maior é {maior}, o menor é {menor}, e a soma é {soma}.")





