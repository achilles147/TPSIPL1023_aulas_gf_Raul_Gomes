#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Introduza a temperatura em Celsius: "))

# C = 5 * ((F - 32) / 9 )
# F =  C ( 9 / 5 ) + 32

farehneit = celsius * ( 9 / 5) + 32

print(f"A temperatura em Farehneit é {farehneit}")