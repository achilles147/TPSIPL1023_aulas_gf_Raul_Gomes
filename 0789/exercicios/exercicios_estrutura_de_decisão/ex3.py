#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

gen = input("Qual o seu género? (F/M)")

if gen == "F" or gen == "f":
    print("O seu género é feminino.")
elif gen == "M" or gen == "m":
    print("O seu género é masculino.")
else:
    print("Sexo inválido.")