import time
import matplotlib.pyplot as plt


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def lucas_with_fib(n):
    return fibonacci(n - 1) + fibonacci(n + 1)


def fib_with_lucas(n):
    i = n // 2
    j = n - i
    return (fibonacci(i) + lucas(j)) * (fibonacci(j) + lucas(i)) // 2


def measure_time(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return end - start


def main():
    max_n = 40
    sizes = list(range(1, max_n + 1, 2))
    
    print("Измеряю время выполнения...")
    
    times_fib = []
    times_fib_lucas = []
    
    for n in sizes:
        t1 = measure_time(fibonacci, n)
        t2 = measure_time(fib_with_lucas, n)
        times_fib.append(t1)
        times_fib_lucas.append(t2)
        print(f"n={n}: fib={t1:.4f}s, fib_lucas={t2:.4f}s")
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_fib, marker='o', label='fibonacci(n)')
    plt.plot(sizes, times_fib_lucas, marker='s', label='fib_with_lucas(n)')
    plt.xlabel('n')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени выполнения')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
