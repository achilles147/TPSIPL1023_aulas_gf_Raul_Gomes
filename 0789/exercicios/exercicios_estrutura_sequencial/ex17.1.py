metros2 = float(input("Insira os metros quadrados a serem pintados:"))
cobertura = metros2 / 6
l_tinta = cobertura // 18 + 1
g_tinta = cobertura // 3.6 + 1

l_mistura = int(cobertura // 18)
resto_tinta = cobertura - (l_mistura * 18)
g_mistura = int((resto_tinta // 3.6)+1)

preco_total_l = l_tinta * 80
preco_total_g = g_tinta * 25
preco_mistura = (l_mistura * 80) + (g_mistura * 25)

print("Latas de tinta necessárias: ", l_tinta)
print("Preço total comprar só latas: ", preco_total_l)

print("Galoes de inta necessários: ", g_tinta)
print("preço total comprar só galoes: ", preco_total_g)

print("Latas de tinta necessárias na mistura: ", l_mistura)
print("Galoes de tinta necessários na mistura: ", g_mistura)
print("Preço total na mistura (latas e galoes): ", preco_mistura)