"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""

num = int(input("Insira um numero: "))
primo = False

for i in range(2, num):
    if (num % i) == 0:
        primo = True
        if primo:
            print(i)
if primo:
    print("não é primo")
else:
    print("é primo")