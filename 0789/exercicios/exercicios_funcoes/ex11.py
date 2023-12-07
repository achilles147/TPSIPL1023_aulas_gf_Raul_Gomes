"""
Data com mês por extenso.

Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

import datetime

def data_extenso(a,m,d):
    x = datetime.date(a,m,d)
    print(x.strftime("%d de %B de %G"))


a = int(input("Ano: "))
m = int(input("Mês: "))
d = int(input("Dia: "))
data_extenso(a,m,d)