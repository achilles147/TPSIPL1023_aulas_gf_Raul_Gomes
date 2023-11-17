"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).

Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
def calc():
    print(f"\nForam exibidos {count} valores.\n")
    for i in range(len(numlist)):
        print(numlist[i], end=" ")
    print("\n")
    numlist.reverse()
    for i in range(len(numlist)):
        print(numlist[i])
    media = soma / count
    print(f"\nA soma dos valores é de {soma}")
    print(f"\nA média dos valores é de {media}")
    acimamedia = 0
    for i in range(len(numlist)):
        if numlist[i] > media:
            acimamedia += 1
    print(f"\nEstão acima da média {acimamedia} valores")
    abaixo7 = 0
    for i in range(len(numlist)):
        if numlist[i] < 7:
            abaixo7 += 1
    print(f"\nEstão abaixo de 7 são {abaixo7} valores")
    print("\nObrigado pela atenção...")

numlist = []
count = 0
soma = 0
while True:
    num = int(input("Nota: "))
    if num == -1:
        break
    count += 1
    soma += num
    numlist.append(num)
calc()

