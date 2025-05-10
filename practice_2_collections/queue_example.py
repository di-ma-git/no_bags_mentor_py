import string
from collections import deque
from queue import PriorityQueue
import random

# Создайте PriorityQueue и добавьте 5 чисел. Выведите их в порядке удаления.

pq = PriorityQueue()

pq.put(3)
pq.put(100)
pq.put(-64)
pq.put(-4)
pq.put(3)
pq.put(1)

while not pq.empty():
    print(pq.get())

# Создайте ArrayDeque, добавьте 5 элементов и выведите их.

adq1 = deque()

[adq1.append(''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 100))))
 for _ in range(0, 5)]

for i in enumerate(adq1, start=1):
    print(i)


# Используйте ArrayDeque как стек: добавьте элементы и извлеките их в обратном порядке.

while adq1:
    print(f"Current size: {len(adq1)}")
    print(f"{adq1.pop()}")


# Используйте ArrayDeque как очередь: добавьте элементы в начало и конец, извлеките из обоих концов.

adq2 = deque()

[adq2.append(''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 100))))
 for _ in range(0, 5)]

adq2.appendleft("begin")

for i in enumerate(adq2, start=1):
    print(i)


adq2.append("end")

for i in enumerate(adq2, start=1):
    print(i)


