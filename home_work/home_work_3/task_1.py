def string_rename(check_string):
    tmp_1 = ''
    tmp_2 = ''
    tmp_string = str(check_string).lower()
    if tmp_string.count('one'):
        tmp_1 += 'one'
        tmp_2 += 'Один'
    elif tmp_string.count('two'):
        tmp_1 += 'two'
        tmp_2 += 'Два'
    elif tmp_string.count('three'):
        tmp_1 += 'three'
        tmp_2 += 'Три'
    elif tmp_string.count('four'):
        tmp_1 += 'four'
        tmp_2 += 'Четыре'
    return str(check_string).lower().replace(tmp_1, tmp_2)


with open('old_list.txt', 'r') as f:
    tmp_str = ''
    for line in f:
        tmp = string_rename(line)
        tmp_str += tmp
    with open('new_list.txt', 'a', encoding="utf-8") as f_2:
        print(tmp_str, file=f_2)
