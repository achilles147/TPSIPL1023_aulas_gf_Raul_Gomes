# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total.

# 1 litro = 3 metros quadrados
# 1 lata = 18 litros = 80,00 R$

metro_quadrado = float(input("Quantos metros quadrados quer pintar? "))

litros = metro_quadrado / 3
qte_latas = litros / 18

print(f"Serão necessários {litros:.2f} litros.")
print(f"Serão necessárias {qte_latas:.0f} latas.")

