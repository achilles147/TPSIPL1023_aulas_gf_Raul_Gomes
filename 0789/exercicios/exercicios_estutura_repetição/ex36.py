"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
informados também pelo usuário, conforme exemplo abaixo:
"""

n_tabuada = int(input("Montar a tabuada de: "))
intervalo_A = int(input("Começar por: "))
intervalo_B = int(input("Terminar em: "))
res = 0
x= 0

if (intervalo_A > intervalo_B):
    x = intervalo_A
    intervalo_A = intervalo_B
    intervalo_B = x

print(f"Vou montar a tabuada de {n_tabuada} começando em {intervalo_A} e terminado em {intervalo_B}:")
for i in range(intervalo_A, intervalo_B + 1):
    res = n_tabuada * i
    print(f"{n_tabuada} x {i} = {res}")