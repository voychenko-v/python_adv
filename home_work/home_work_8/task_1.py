from datetime import datetime


def save_info_class(sam_class):
    def wrapper(*args, **kwargs):
        with open('save_info_class.txt', 'a', encoding='utf-8') as f:
            print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                  f' Создан экземпляр класса {sam_class}'
                  f' по адресу памяти {hex(id(sam_class))}', file=f)
        return sam_class(*args, **kwargs)
    return wrapper


@save_info_class
class Test:
    def __init__(self, tmp, tmp2):
        self.tmp = tmp
        self.tmp2 = tmp2


tmp_t = Test(3, 4)
print(tmp_t)

