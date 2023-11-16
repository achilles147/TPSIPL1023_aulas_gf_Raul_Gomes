"""
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números
primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
"""
num_max = int(input("Até que número? "))


for i in range(2, num_max):
    primo = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
"""

end = int(input("Até que número quer calcular? "))

for i in range(2, end+1):
    flag = 0
    for j in range(2, i):
        if (i % j == 0):
            flag = 1
    if (flag == 0):
        print(i, end=" ")


