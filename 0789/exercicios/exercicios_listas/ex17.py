"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.

 A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

while True:
    saltos = 0
    media = 0
    nome_atleta = str(input("Atleta: "))
    if nome_atleta == "":
        break
    salto1 = float(input("\nPrimeiro Salto: "))
    salto2 = float(input("Segundo Salto: "))
    salto3 = float(input("Terceiro Salto: "))
    salto4 = float(input("Quarto Salto: "))
    salto5 = float(input("Q1uinto Salto: "))
    saltos = salto1 + salto2 + salto3 + salto4 + salto5
    media = saltos / 5

    print(f"""
    Resultado final:
    Atleta: {nome_atleta}
    Saltos: {salto1} - {salto2} - {salto3} - {salto4} - {salto5}
    Media dos saltos: {media:.2f} m
    """)