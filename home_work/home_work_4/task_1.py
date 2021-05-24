def factorial_iter(num):
    num_factorial = 1
    for i in range(2, num + 1):
        num_factorial *= i
        yield num_factorial


fac = factorial_iter(5)

for i in fac:
    print(i)

