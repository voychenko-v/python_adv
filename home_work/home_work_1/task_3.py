def max_sum(a, b, c):
    list_arg = [a, b, c]
    list_arg.sort()
    nam_sum = list_arg[-1] + list_arg[-2]
    return print(f'Сумма найбольших двух аргументов из {a,b,c} равна: {nam_sum}')


max_sum(6, 2, 4)
