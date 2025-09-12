import timeit
import matplotlib.pyplot as plt
import random

def experiment():
    sizes = [100, 1000, 10000, 50000]
    list_times = []
    set_times = []
    
    for size in sizes:
        element_to_find = size // 2
        
        list_time = timeit.timeit(
            f"{element_to_find} in list(range({size}))",
            number=1000
        )
        
        set_time = timeit.timeit(
            f"{element_to_find} in set(range({size}))",
            number=1000
        )
        
        list_times.append(list_time)
        set_times.append(set_time)
        
        ratio = list_time / set_time
        print(f"{size:6} | {list_time:6.3f} | {set_time:8.3f} | {ratio:12.1f}x")

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, list_times, 'r-o', label='Список')
    plt.plot(sizes, set_times, 'g-o', label='Множество')
    plt.xlabel('Размер данных')
    plt.ylabel('Время (секунды)')
    plt.title('Оператор in: Список vs Множество')
    plt.legend()
    plt.grid(True)
    plt.show()

experiment()