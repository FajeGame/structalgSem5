import time
import random
import statistics
import matplotlib.pyplot as plt


def measure_membership_list(size, queries):
    data = list(range(size))
    start = time.perf_counter()
    for q in queries:
        _ = q in data
    end = time.perf_counter()
    return (end - start) / len(queries)


def measure_membership_set(size, queries):
    data = set(range(size))
    start = time.perf_counter()
    for q in queries:
        _ = q in data
    end = time.perf_counter()
    return (end - start) / len(queries)


def experiment():
    random.seed(42)
    sizes = [100, 1_000, 5_000, 10_000, 50_000, 100_000]
    repeats = 7
    queries_per_repeat = 10_000

    list_times = []
    set_times = []

    for size in sizes:
        lt = []
        st = []
        for _ in range(repeats):
            # Половина запросов попадает в структуру, половина — мимо
            hits = [random.randint(0, size - 1) for _ in range(queries_per_repeat // 2)]
            misses = [size + random.randint(1, size) for _ in range(queries_per_repeat // 2)]
            queries = hits + misses
            random.shuffle(queries)

            lt.append(measure_membership_list(size, queries))
            st.append(measure_membership_set(size, queries))

        lt_med = statistics.median(lt)
        st_med = statistics.median(st)
        list_times.append(lt_med)
        set_times.append(st_med)
        print(size, lt_med)
        print(size, st_med)

    plt.figure(figsize=(9, 5))
    plt.plot(sizes, list_times, 'r-o', label='Список (медиана, на 1 запрос)')
    plt.plot(sizes, set_times, 'g-o', label='Множество (медиана, на 1 запрос)')
    plt.xlabel('Размер структуры данных')
    plt.ylabel('Время одного запроса (сек)')
    plt.title('Оператор in: Список vs Множество (рандомизация, многократные прогоны)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


experiment()