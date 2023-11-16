"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""


nome = input("Nome: ")
while len(nome) < 3:
    print("Nome inválido: menos que 3 caracteres!")
    nome = input("Nome: ")

idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida: menos que 0 ou mais que 150 anos! ")
    idade = int(input("Idade: "))

salario = float(input("Salário: "))
while salario < 0:
    print("Salário inválido: menor que 0! ")
    salario = float(input("Salário: "))

sexo = input("Sexo (f, m): ")
while sexo != 'f' and sexo != 'm':
    print("Sexo inválido: caracter inválido!")
    sexo = input("Sexo (f, m): ")

est_civil = input("Estado civil (s, c, v, d): ")
while est_civil != 's' and est_civil != 'c' and est_civil != 'v' and est_civil != 'v':
    print("Estado civil inválido: caracter inválido!")
    est_civil = input("Estado civil (s, c, v, d): ")

print(f"\nNome: {nome} (válido)")
print(f"\nIdade: {idade} (válido)")
print(f"\nSalário: {salario:.2f} (válido)")
print(f"\nSexo: {sexo} (válido)")
print(f"\nEstado civil: {est_civil} (válido)")

