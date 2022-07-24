import matplotlib.pyplot as plt
import numpy as np

from random import random
from time import time

chests = [0]*400
iters = 1_000_000
timestamp = time()
all_chests = []
timer = 0

for i in range(1, iters+1):
    if not i % (iters/1000) and timer==0: timer = time()-timestamp; print(f'Осталось примерно {(1000*timer - 1000*timer*i/iters)/60:.2f}m')
    if not i % (iters/10): print(f'{i/iters:.0%} {1000*timer - 1000*timer*i/iters:.2f}s')

    c = 0
    for _ in range(400):
        if random() <= 0.0425: c += 1
    chests[c] += 1
    all_chests.append(c)

fig, ax = plt.subplots()
nonzero = sum([1 for _ in chests if _ > 0])
x = [_+.5 for _ in range(nonzero)]
y = [i/iters for i in chests[:nonzero]]

# print(f'{x=}, {y=}, {chests=}')
print(f'\nНа {iters:,} проходов \nНенулевых значений: {nonzero}')
print(f'Среднее: {sum([i*chests[i] for i in range(len(chests))])/iters}\n')
for i in (17, 24, 28, 30, 40, 50):
    if nonzero >= i:
        if i <= 30: print(f'Для {i}: {chests[i]} {y[i]:.3%}')
        else: print(f'Для {i}: {chests[i]} {y[i]:.6%}')
print(f'\nМаксимум {nonzero-1}: {chests[nonzero-1]} {y[nonzero-1]:.8%}\n')
print(f'Сумма: {sum(y):.4}')
print(f'До 17: {sum(y[:17]):.3%}')
print(f'После 17: {sum(y[17:]):.3%}')
print(f'От 14 до 20: {sum(y[14:20]):.3%}')
print(f'От 20 до 30: {sum(y[20:30]):.3%}')
print(f'От 30: {sum(y[30:]):.3%}')

ax.set(xlim=(0, nonzero-1), ylim=(0, max(y)*1.05))
ax.plot(x, y, linewidth=2)
ax.hist(all_chests, bins=range(0,nonzero-1), weights=np.ones(len(all_chests)) / len(all_chests), color=(0.1, 0.2, 0.5, 0.3))
plt.show()
