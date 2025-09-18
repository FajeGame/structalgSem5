import time
import random
import statistics
import matplotlib.pyplot as plt


def measure_deletions_list(size, deletions):
    base = list(range(size))
    # Удаляем по индексам в порядке убывания, чтобы не тратить время на пересчёт позиций
    indices = sorted(random.sample(range(size), deletions), reverse=True)
    start = time.perf_counter()
    for idx in indices:
        del base[idx]
    end = time.perf_counter()
    return (end - start) / deletions


def measure_deletions_dict(size, deletions):
    dct = {i: i for i in range(size)}
    keys = random.sample(range(size), deletions)
    start = time.perf_counter()
    for k in keys:
        del dct[k]
    end = time.perf_counter()
    return (end - start) / deletions


def experiment():
    random.seed(42)
    sizes = [100, 1_000, 5_000, 10_000, 50_000, 100_000]
    repeats = 7

    list_times = []
    dict_times = []

    for size in sizes:
        deletions = min(2_000, max(10, size // 5))
        lt = []
        dt = []
        for _ in range(repeats):
            lt.append(measure_deletions_list(size, deletions))
            dt.append(measure_deletions_dict(size, deletions))
        lt_med = statistics.median(lt)
        dt_med = statistics.median(dt)
        list_times.append(lt_med)
        dict_times.append(dt_med)
        print(size, lt_med)
        print(size, dt_med)

    plt.figure(figsize=(9, 5))
    plt.plot(sizes, list_times, 'r-o', label='Список (медиана, на 1 удаление)')
    plt.plot(sizes, dict_times, 'b-o', label='Словарь (медиана, на 1 удаление)')
    plt.xlabel('Размер структуры данных')
    plt.ylabel('Время на одно удаление (сек)')
    plt.title('Удаление: Список vs Словарь (рандомизация, многократные прогоны)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


experiment()