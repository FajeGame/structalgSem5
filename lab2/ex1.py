import random
import time
from typing import List, Callable, Tuple


def selection_sort(data: List[int]) -> List[int]:

    arr = data[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quicksort_iterative(data: List[int]) -> List[int]:

    arr = data[:]
    stack: List[Tuple[int, int]] = [(0, len(arr) - 1)]

    def partition(lo: int, hi: int) -> int:
        mid = lo + (hi - lo) // 2
        pivot = arr[mid]
        i, j = lo, hi
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i, j

    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        i, j = partition(lo, hi)
        if lo < j:
            stack.append((lo, j))
        if i < hi:
            stack.append((i, hi))
    return arr


def generate_data(kind: str, n: int, seed: int = 42) -> List[int]:
    rnd = random.Random(seed)
    if kind == "random":
        return [rnd.randint(0, 10_000_000) for _ in range(n)]
    elif kind == "sorted":
        return list(range(n))
    elif kind == "reversed":
        return list(range(n, 0, -1))
    else:
        raise ValueError(f"Unknown data kind: {kind}")


def benchmark_once(algorithm: Callable[[List[int]], List[int]], data: List[int]) -> float:
    start = time.perf_counter()
    result = algorithm(data)
    end = time.perf_counter()
    return end - start


def benchmark(algorithm: Callable[[List[int]], List[int]], kind: str, sizes: List[int], repeats: int, seed: int) -> List[float]:
    times: List[float] = []
    for n in sizes:
        total = 0.0
        for r in range(repeats):
            data = generate_data(kind, n, seed + r)
            total += benchmark_once(algorithm, data)
        times.append(total / repeats)
    return times


def plot_on_axis(ax, sizes: List[int], y1: List[float], y2: List[float], kind_label: str) -> None:
    ax.plot(sizes, y1, marker="o", label="Selection sort")
    ax.plot(sizes, y2, marker="s", label="Quicksort (iterative)")
    ax.set_xlabel("n")
    ax.set_ylabel("Время (с)")
    ax.set_title(kind_label)
    ax.grid(True, alpha=0.3)
    ax.legend()


def main():
    sizes = [100, 200, 400, 800, 1200, 1600]
    repeats = 3
    seed = 42

    algorithms = [
        (selection_sort, "Selection sort"),
        (quicksort_iterative, "Quicksort (iterative)"),
    ]

    kinds = [
        ("random", "Случайные числа"),
        ("sorted", "Отсортированный список"),
        ("reversed", "Обратный порядок"),
    ]

    results = []
    for kind_key, kind_label in kinds:
        t1 = benchmark(algorithms[0][0], kind_key, sizes, repeats, seed)
        t2 = benchmark(algorithms[1][0], kind_key, sizes, repeats, seed)
        results.append((kind_label, t1, t2))

    # Отрисовка на одной фигуре
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
    for ax, (kind_label, t1, t2) in zip(axes, results):
        plot_on_axis(ax, sizes, t1, t2, kind_label)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


