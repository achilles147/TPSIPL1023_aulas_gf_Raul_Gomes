#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Por favor, introduza o raio de um círculo: "))

# area de um circulo = raio^2 * pi

area_circulo = 3.141 * raio**2

print(f"A area do circulo é {area_circulo}")