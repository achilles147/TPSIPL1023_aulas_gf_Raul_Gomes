"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""

"""
# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
"""

ano = int(input("Insira um ano: "))





if ano % 100 == 0 and ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"Não é ano bissexto.")
