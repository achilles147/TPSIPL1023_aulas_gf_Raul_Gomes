
a, b = 0, 1
n = int(input("Sequenciar Fibonacci: "))


for i in range(n):
    a, b = b, a + b
    print(a)


