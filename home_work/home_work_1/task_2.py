def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


# Ниже введите число
fib_num = 12
fib = fibonacci(fib_num)

print(f'Число Фибоначчи под номером {fib_num} равно: {fib}')


assert fibonacci(7) == 13
