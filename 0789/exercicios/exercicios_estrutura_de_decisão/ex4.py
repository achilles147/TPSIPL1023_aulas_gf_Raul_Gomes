#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

char = input("Digite um caractere:")

if  (char == "A" or
    char == "a" or
    char == "E" or
    char == "e" or
    char == "I" or
    char == "i" or
    char == "O" or
    char == "o" or
    char == "U" or
    char == "u" ):
    print("O seu caractere é uma vogal")
else:
    print("O seu caractere é uma consoante.")

