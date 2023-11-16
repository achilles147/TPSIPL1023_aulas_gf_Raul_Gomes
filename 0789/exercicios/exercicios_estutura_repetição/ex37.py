"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do
mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""



altura_maior = 0
altura_menor = 300
peso_maior = 0
peso_menor = 500
valido = True

while valido:
    codigo = int(input("Qual o seu código (1-200): "))
    if codigo == 0:
        break
    altura = float(input("Qual a sua altura (cm): "))
    peso = float(input("Qual o seu pêso (kg): "))


    if altura > altura_maior:
        altura_maior = altura
        cod_altura_maior = codigo
    if peso > peso_maior:
        peso_maior = peso
        cod_peso_maior = codigo

    if altura < altura_menor:
        altura_menor = altura
        cod_altura_menor = codigo
    if peso < peso_menor:
        peso_menor = peso
        cod_peso_menor = codigo

print(f"O cliente mais alto tem o código {cod_altura_maior} com altura de {altura_maior}")
print(f"O cliente mais alto tem o código {cod_altura_menor} com altura de {altura_menor}")
print(f"O cliente mais alto tem o código {cod_peso_maior} com altura de {peso_maior}")
print(f"O cliente mais alto tem o código {cod_peso_menor} com altura de {peso_menor}")

