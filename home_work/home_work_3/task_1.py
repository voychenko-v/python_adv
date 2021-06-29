def string_rename(check_string):
    dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for key in dict_num:
        if check_string.count(key):
            return check_string.replace(key, dict_num[key])


with open('old_list.txt', 'r', encoding="utf-8") as f:
    with open('new_list.txt', 'a', encoding="utf-8") as f_2:
        for line in f:
            tmp = string_rename(line)
            if tmp is None:
                tmp = line
            print(tmp, file=f_2, end='')
