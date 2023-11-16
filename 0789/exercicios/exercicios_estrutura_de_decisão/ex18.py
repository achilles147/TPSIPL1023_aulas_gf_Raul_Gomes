"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
"""

data_input = input("Insira uma data no formato dd/mm/aaaa: ")
ano = data_input[6:]
mes = data_input[3:5]
dia = data_input[0:2]


if int(ano) % 100 == 0 and int(ano) % 400 == 0:
    print(f"O ano {ano} é bissexto.")
    if int(ano) > 0 and int(ano) <= 2024:
        print("Ano válido.")
        if int(mes) > 0 and int(mes) < 13:
            print("Mês válido.")
            if int(mes) % 2 == 0:
                if int(mes) == 2:
                    if int(dia >= 0 and int(dia) <= 29):
                        print("Dia válido.")
                        print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                    else:
                        print("Dia inválido -> maior que 29 ou menor que 0")
                else:
                    if int(dia) >= 0 and int(dia) <= 30:
                        print("Dia válido.")
                        print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                    else:
                        print("Dia inválido -> maior que 30 ou menor que 0 -> Data Inválida")
            else:  # mês impar
                if int(dia) >= 0 and int(dia) <= 31:
                    print("Dia válido.")
                    print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                else:
                    print("Dia inválido -> maior que 31 ou menor que 0 -> Data Inválida")
        else:
            print("Mês inválido -> maior que 12 ou menor que 1 -> Data Inválida")
    else:
        print("Ano inválido -> maior que 2024 ou menor que 0 -> Data Inválida")
elif int(ano) % 4 == 0 and int(ano) % 100 != 0:
    print(f"O ano {ano} é bissexto.")
    if int(ano) > 0 and int(ano) <= 2024:
        print("Ano válido.")
        if int(mes) > 0 and int(mes) < 13:
            print("Mês válido.")
            if int(mes) % 2 == 0:
                if int(mes) == 2:
                    if int(dia) >= 0 and int(dia) <= 29:
                        print("Dia válido.")
                        print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                    else:
                        print("Dia inválido -> maior que 29 ou menor que 0")
                else:
                    if int(dia) >= 0 and int(dia) <= 30:
                        print("Dia válido.")
                        print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                    else:
                        print("Dia inválido -> maior que 30 ou menor que 0 -> Data Inválida")
            else:  # mês impar
                if int(dia) >= 0 and int(dia) <= 31:
                    print("Dia válido.")
                    print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                else:
                    print("Dia inválido -> maior que 31 ou menor que 0 -> Data Inválida")
        else:
            print("Mês inválido -> maior que 12 ou menor que 1 -> Data Inválida")
    else:
        print("Ano inválido -> maior que 2024 ou menor que 0 -> Data Inválida")
else:
    if int(ano) > 0 and int(ano) <= 2024:
        print("Ano válido.")
        if int(mes) > 0 and int(mes) < 13:
            print("Mês válido.")
            if int(mes) % 2 == 0:
                if int(mes) == 2:
                    if int(dia >= 0 and int(dia) <= 28):
                        print("Dia válido.")
                        print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                    else:
                        print("Dia inválido -> maior que 29 ou menor que 0")
                else:
                    if int(dia) >= 0 and int(dia) <= 30:
                        print("Dia válido.")
                        print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                    else:
                        print("Dia inválido -> maior que 30 ou menor que 0 -> Data Inválida")
            else:  # mês impar
                if int(dia) >= 0 and int(dia) <= 31:
                    print("Dia válido.")
                    print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                else:
                    print("Dia inválido -> maior que 31 ou menor que 0 -> Data Inválida")
        else:
            print("Mês inválido -> maior que 12 ou menor que 1 -> Data Inválida")
    else:
        print("Ano inválido -> maior que 2024 ou menor que 0 -> Data Inválida")



""" # validação da data
if int(ano) > 0 and int(ano) < 2024:
    print("Ano válido.")
    if int(mes) > 0 and int(mes) < 13: #indica se é mês válido
        print("Mês válido.")
        if int(mes) % 2 == 0: #mês par
            if int(mes) == 2:
                if int(dia >= 0 and int(dia) <= 29)
                    print("Dia válido")
                    print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                else: 
                    print("Dia inválido -> maior que 29 ou menor que 0")           
            else:
                if int(dia) >= 0 and int(dia) <= 30:
                    print("Dia válido.")
                    print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
                else:
                    print("Dia inválido -> maior que 30 ou menor que 0 -> Data Inválida")
        else: #mês impar
            if int(dia) >= 0 and int(dia) <= 31:
                print("Dia válido.")
                print(f"\n\n A sua data é {dia}/{mes}/{ano}. Data Válida!")
            else:
                print("Dia inválido -> maior que 31 ou menor que 0 -> Data Inválida")
    else:
        print("Mês inválido -> maior que 12 ou menor que 1 -> Data Inválida")
else:
    print("Ano inválido -> maior que 2024 ou menor que 0 -> Data Inválida")"""


""" # validação ano bissexto
if ano % 100 == 0 and ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"Não é ano bissexto.")"""






