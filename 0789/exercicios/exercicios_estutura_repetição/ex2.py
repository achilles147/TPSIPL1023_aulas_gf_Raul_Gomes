"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.

"""

user = input("Insira o seu nome de usuário: ")
password = input("Insira a sua palavra chave: ")

user = user.lower()
password = password.lower()

while user == password:
    print("\tO seu nome de usuário é igual à sua palavra chave.\n\tAutenticação inválida.")
    user = input("Insira o seu nome de usuário: ")
    password = input("Insira a sua palavra chave: ")
print("Autenticação válida!")