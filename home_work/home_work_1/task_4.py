

def enter_num():
    num_string = input('Введите числа: ')
    list_num = num_string.split()
    return list_num


def check(check_data):
    for i in check_data:
        if i == '$':
            return False


def sum_num(list_num):
    sum_argument = 0
    for i in list_num:
        if i.isdigit():
            i = int(i)
            sum_argument += i
    return sum_argument


def main():
    print(
        '- Для получения суммы чисел введите их через пробел и нажмите Enter.\n'
        '- Для окончания подсчотов введите в строке символ "$".\n'
        '- Если перед символом "$" были цифры, они просуммируются.\n'
        )
    count_sum = 0
    while True:
        list_data = enter_num()
        check_f = check(list_data)
        if check_f is False:
            count_sum += sum_num(list_data)
            print(f'Сумма всех чисел равна: {count_sum}\n'
                  'Выход из программы!')
            break
        count_sum += sum_num(list_data)
        print(f'Сумма чисел равна: {count_sum}. Введите еще числа для суммирования.\n')
    return


if __name__ == "__main__":
    main()
