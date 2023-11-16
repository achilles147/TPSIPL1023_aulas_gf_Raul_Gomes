"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
arr1 = []
arr2 = []
for i in range(10):
    arr1.append(i)
    arr2.append(i+10)
print(arr1)
print(arr2)

arr3 = arr1 + arr2
print(arr3)