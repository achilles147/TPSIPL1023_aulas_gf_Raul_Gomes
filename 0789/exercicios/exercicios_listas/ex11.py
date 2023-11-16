"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

arr1 = []
arr2 = []
arr4 = []
for i in range(10):
    arr1.append(i)
    arr2.append(i+10)
    arr4.append(i+20)
print(arr1)
print(arr2)
print(arr4)
arr3 = arr1 + arr2 + arr4
print(arr3)