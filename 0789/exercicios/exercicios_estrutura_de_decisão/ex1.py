# Faça um Programa que peça dois números e imprima o maior deles

x = float(input("Insira um numero:"))
y = float(input("Insira um outro numero:"))

if x > y:
    print("O numero maior é ", x)
elif y > x:
    print("O numero maior é ", y)
elif y == x:
    print("Os numeros são iguais.")
