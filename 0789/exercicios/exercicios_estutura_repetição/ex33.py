"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que
leia as um conjunto indeterminado de temperaturas, e informe ao final a
menor e a maior temperaturas informadas, bem como a média das temperaturas.

"""

temp = float(input("Insira a temperatura: "))
maior = 0
menor = 100

while (temp > -100):
    if temp > maior:
        maior = temp
    elif temp < menor:
        menor = temp
    try:
        temp = float(input("Insira a temperatura: "))
    except ValueError:
        print("Fim")
        break
print(f"A temperatura maior é {maior} e a menor é {menor}")

