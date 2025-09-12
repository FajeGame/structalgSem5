import timeit
import matplotlib.pyplot as plt
import random

def experiment():
    sizes = [100, 1000, 10000]
    list_times = []
    dict_times = []
    
    for size in sizes:
        list_time = timeit.timeit(
            f"lst = list(range({size})); del lst[{size//2}]", 
            number=1000
        )
        
        dict_time = timeit.timeit(
            f"dct = {{i: 'val' for i in range({size})}}; del dct[{size//2}]", 
            number=1000
        )
        
        list_times.append(list_time)
        dict_times.append(dict_time)
        
        ratio = list_time / dict_time
        print(f"{size:6} | {list_time:11.4f} | {dict_time:12.4f} | {ratio:18.1f}x")
    
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, list_times, 'r-o', label='Список')
    plt.plot(sizes, dict_times, 'b-o', label='Словарь')
    plt.xlabel('Размер данных')
    plt.ylabel('Время (секунды)')
    plt.title('del: Список vs Словарь')
    plt.legend()
    plt.grid(True)
    plt.show()

experiment()