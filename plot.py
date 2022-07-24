import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

f = open('data.txt', 'r').read().splitlines()
f.pop(0); f.pop(0); f.pop(0)
f = [_.split() for _ in f]

for _ in range(len(f)):
    f[_] = list(filter(lambda x: x not in ('+', '-', '=', '|'), f[_]))
    
    for i in range(11 if len(f[_]) > 13 else 9):
        f[_][i] = int(f[_][i].replace(',', ''))
    
# Chests
fig, axs = plt.subplot_mosaic([['chests', 'cycle'],
                            ['chests', 'percentage']], figsize=(8.5, 4.5), constrained_layout=True)

fig.canvas.manager.set_window_title('Chests')
ax = list(axs.items())
text = ''

for data in ((-8, '#EC7063', 'o Common'),  (-7, '#F5B041', '8 Double'), (-6, '#5DADE2', 'Ω Gamma'), (-5, '#A569BD', '∆ Delta')):
    x, y = [_ for _ in range(len(f))], []
    for _ in range(len(f)): y.append(y[-1]+f[_][data[0]] if len(y)>0 else f[_][data[0]])
    ax[0][1].plot(x, y, c=data[1], label=data[2], linewidth=3)
    ax[0][1].legend()

    x, y = [len(f)-_ for _ in range(26)], []
    for _ in range(-26, 0, 1): y.insert(0, (f[_][data[0]]))
    ax[1][1].plot(x, y, c=data[1], linewidth=3)

    x, y = [_ for _ in range(len(f)-1)], []
    for _ in range(1, len(f)): 
        chests, all_chests = 0, 0
        for i in range(_):
            chests += f[i][data[0]]
            all_chests += f[i][-8] + f[i][-7] + f[i][-6] + f[i][-5]
        
        y.append(chests / all_chests)
    ax[2][1].plot(x, y, c=data[1] ,linewidth=3)
    text += f'{data[2][0]}: {round(chests/all_chests*100, 2)}%\n'

ax[0][1].set(xlim=(0, len(f)), ylim=(0, round(sum([*map(lambda x: x[-7], f[:])]), -3)+5_000))
ax[0][1].set_title('Chests')
ax[0][1].set_ylabel('Total number of chests')

ax[1][1].set(xlim=(len(f)-25, len(f)), ylim=(0, 250))
ax[1][1].set_title('Distribution per cycle')
ax[1][1].set_ylabel('Chests')

ax[2][1].text(len(f)*0.78, 0.48, text, clip_on=True)
ax[2][1].yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax[2][1].set(xlim=(0, len(f)), ylim=(0, 1))
ax[2][1].set_title('Percentage distribution')

# Resources
fig, axs = plt.subplot_mosaic([['xi', 'gearpoints'],
                            ['xi', 'crystals']], figsize=(8.5, 4.5), constrained_layout=True)

fig.canvas.manager.set_window_title('Resources')
ax = list(axs.items())

x, y = [], []
for _ in range(len(f)): 
    if len(f[_]) > 13:
        x.append(_); y.append(f[_][5])
ax[1][1].plot(x, y, c='#AAAAAA', label='@ Gp', linewidth=3)

x, y = [_ for _ in range(len(f))], []
for _ in range(len(f)): y.append(f[_][4])
ax[0][1].plot(x, y, c='#F4D03F', label='@ Ki', linewidth=3)

x, y = [], []
for _ in range(len(f)): 
    if len(f[_]) > 13:
        x.append(_); y.append(f[_][6])
ax[2][1].plot(x, y, c='#A569BD', linewidth=3)

ax[0][1].set(xlim=(0, len(f)))
ax[0][1].set_title('@ Ki')
ax[0][1].set_ylabel('Value in inventory')

ax[1][1].set(xlim=(572, len(f)-1))
ax[1][1].set_title('* Gp')

ax[2][1].set_title('♦ Crystals')
ax[2][1].set(xlim=(572, len(f)-1))

plt.show()
