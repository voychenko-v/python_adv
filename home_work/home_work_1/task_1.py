import time


def time_work(func):
    def wrapper(*args, **kwargs):
        # Добавил 1 секунду сна для проверки работы функции
        time_start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        time_w = time.time() - time_start
        print(f'Время работы функции {time_w} сек.')
    return wrapper


@time_work
def list_generate():
    l = []
    for i in range(100):
        l.append(i)
    return print(l)


list_generate()