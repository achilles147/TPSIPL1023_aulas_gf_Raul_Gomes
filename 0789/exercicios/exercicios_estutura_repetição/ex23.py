"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
num = int(input("Insira um numero: "))
primo = False

for i in range(2, num):
    if (num % i) == 0:
        primo = True
        res = num / i
        print(f"{num} / {i} = {res}")
if primo:
    print("não é primo")
else:
    print("é primo")