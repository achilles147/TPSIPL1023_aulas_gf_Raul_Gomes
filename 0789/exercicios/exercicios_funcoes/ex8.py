"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""
def qte_digitos(num):
    i = 0
    while True:
        try:
            num[i]
            i += 1
        except:
            break
    print(i)


num = input("Numero: ")
qte_digitos(num)

