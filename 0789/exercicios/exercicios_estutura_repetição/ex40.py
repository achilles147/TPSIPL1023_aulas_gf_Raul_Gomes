"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:

Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
menor = 100000
maior = 0
soma = 0
soma_ac = 0
n_cidades_menor2000 = 0

for i in range(5):
    print(f"\nCidade {i+1}")
    codigo_cidade = input("Código: ")
    qte_veiculos_passeio = int(input("Veículos de passeio: "))
    qte_acidentes_de_transito_com_vitimas = int(input("Acidentes de trânciso com vítimas: "))

    if qte_acidentes_de_transito_com_vitimas < menor:
        menor = qte_acidentes_de_transito_com_vitimas
        codigo_cidade_menor_acidentes = codigo_cidade
    elif qte_acidentes_de_transito_com_vitimas > maior:
        maior = qte_acidentes_de_transito_com_vitimas
        codigo_cidade_maior_acidentes = codigo_cidade

    if qte_veiculos_passeio < 2000:
        n_cidades_menor2000 += 1
        soma_ac += qte_acidentes_de_transito_com_vitimas

    soma += qte_acidentes_de_transito_com_vitimas

media = soma / 5
media2000 = soma_ac / n_cidades_menor2000

print(f"\nO maior indice de acidentes foi {maior} na cidade {codigo_cidade_maior_acidentes}")
print(f"O menor indice de acidentes foi {menor} na cidade {codigo_cidade_menor_acidentes}")
print(f"A média de acidentes nas cidades foi de {media:.2f} acidentes")
print(f"A média de acidentes nas cidades com menos de 2000 veículos foi de {media2000:.2f}")