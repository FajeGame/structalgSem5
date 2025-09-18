import time 
import matplotlib.pyplot as plt
import random
import string


def pal1(word):
    word_reversed = reversed(word)
    comparisons = [i == j for i, j in zip(word, word_reversed)]
    return all(comparisons)
    

def pal2(word):
    return word == word[::-1]

x1 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
y1 = []
y2 = []

# Генерация данных и многократные прогоны для стабильных измерений
SAMPLES_PER_LENGTH = 200
PALINDROME_SHARE = 0.5

def _rand_string(n):
    alphabet = string.ascii_lowercase
    return ''.join(random.choice(alphabet) for _ in range(n))

def _rand_palindrome(n):
    if n <= 1:
        return 'a' * max(1, n)
    half = (n + 1) // 2
    left = _rand_string(half)
    if n % 2 == 0:
        return left + left[::-1]
    return left + left[-2::-1]

for i in range(10): 
    n = x1[i]
    num_pal = int(SAMPLES_PER_LENGTH * PALINDROME_SHARE)
    num_non = SAMPLES_PER_LENGTH - num_pal
    dataset = [_rand_palindrome(n) for _ in range(num_pal)] + [_rand_string(n) for _ in range(num_non)]
    random.shuffle(dataset)

    start_time = time.perf_counter()
    for s in dataset:
        pal1(s)
    end_time = time.perf_counter()
    y1.append((end_time - start_time) / len(dataset))

for i in range(10): 
    n = x1[i]
    num_pal = int(SAMPLES_PER_LENGTH * PALINDROME_SHARE)
    num_non = SAMPLES_PER_LENGTH - num_pal
    dataset = [_rand_palindrome(n) for _ in range(num_pal)] + [_rand_string(n) for _ in range(num_non)]
    random.shuffle(dataset)

    start_time = time.perf_counter()
    for s in dataset:
        pal2(s) 
    end_time = time.perf_counter()
    y2.append((end_time - start_time) / len(dataset))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'ro-')
plt.title('pal1 - Медленная реализация')
plt.xlabel('Длина строки')
plt.ylabel('Время выполнения (сек)')

plt.subplot(1, 2, 2)
plt.plot(x1, y2, 'go-')
plt.title('pal2 - Быстрая реализация')
plt.xlabel('Длина строки')
plt.ylabel('Время выполнения (сек)')

plt.tight_layout()
plt.show()

print("Асимптотическая сложность:")
print("pal1: O(n) - линейная сложность")
print("pal2: O(n) - линейная сложность")