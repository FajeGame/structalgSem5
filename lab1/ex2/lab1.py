import time 
import matplotlib.pyplot as plt

def pal1(word):
    word_reversed = reversed(word)
    comparisons = [i == j for i, j in zip(word, word_reversed)]
    return all(comparisons)
    
def pal2(word):
    return word == word[::-1]

x = ['a', 
    'aaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']

x1 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
y1 = []
y2 = []

for i in range(10): 
    start_time = time.time()
    pal1(x[i])
    end_time = time.time()
    y1.append(end_time - start_time)

for i in range(10): 
    start_time = time.time()
    pal2(x[i]) 
    end_time = time.time()
    y2.append(end_time - start_time)

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