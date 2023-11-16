"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos).
"""
import datetime


file_size = float(input("Insira o tamanho do arquivo (em MB):"))
download_speed = float(input("Insira a velocidade de Internet (MBps):"))

file_bit_size = file_size * 8
n = file_bit_size / download_speed


minutos = n // 60
segundos = (n % 60)
print(f"Esta transferência durará {int(minutos)} minutos e {int(segundos)} segundos.")






"""

Since we need the number of hours, we will divide the total number of seconds (n) by the total number of seconds in an hour (3600).

horas = n // 3600


To calculate the value of minutes we need to first divide the total number of seconds by 3600 and take the remainder.

n = n % 3600

Now to calculate the value of minutes from the above result we will again use the floor operator.

minutos = n // 60

To get seconds value we again need to divide the total number of seconds by the number of seconds in one minute (60) and take the remainder.

segundos = n % 60

print("\nEsta transferência vai demorar: ")
print(f"Horas: {int(horas)}")
print(f"Minutos: {int(minutos)}")
print(f"Segundos: {int(segundos)}")


# metodo 1 com date formatting
horas = n // 3600
segundos = n % 60
n = n % 3600
minutos = n // 60
print("\nEsta transferência vai demorar: %dh:%dm:%ds"%(horas,minutos,segundos))

# metodo 2 (com datetime.divmod)
m, s = divmod(n, 60)
h, m = divmod(m, 60)
print(f"\nEsta transferência vai demorar: {h:.0f}h:{m:.0f}m:{s:.0f}s\n")"""

