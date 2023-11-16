"""
Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

"""

idade = float(input("Que idade tem? "))
pessoa = 0
soma_idades = 0


while (idade > 0):
    pessoa += 1
    soma_idades += idade
    try:
        idade = float(input("Que idade tem? "))
    except ValueError:
        break


media = soma_idades / pessoa
print(f"Média de idades: {media:.1f} anos")

if media > 0 and media <= 25:
    print("A turma é jovem.")
elif media > 25 and media <= 60:
    print("A turma é adulta.")
elif media > 60:
    print("A turma é idosa.")

