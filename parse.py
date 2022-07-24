f = open('data.txt', 'r')
f = f.read().split('\n')
f = f[3:-1]

c1, c2, c3, c4 = 0, 0, 0, 0
max1, max2, max3, max4 = 0, 0, 0, 0

plateau_15 = []
locs_data = dict()

for i in range(len(f)): 
    t = [*map(int, f[i][122:138].split())]

    if i != 0:
        if '15* Плато' in f[i-1]: plateau_15.append(f[i][122:138])
        
        location = f[i-1][140:150]
        if location not in locs_data:
            locs_data[location] = [0, 0]

        if sum(t) == 400: locs_data[location][0] += 1
        else: locs_data[location][1] += 1
 
    c1 += t[0]
    c2 += t[1]
    c3 += t[2]
    c4 += t[3]
    if max1 < t[0]: max1 = t[0]
    if max2 < t[1]: max2 = t[1]
    if max3 < t[2]: max3 = t[2]
    if max4 < t[3]: max4 = t[3]

P = '\033[1;35m'
W = '\033[0m'
chests = c1+c2+c3+c4
print(f'o: {P}{c1}{W}, ({round(c1/chests*100, 2)}%), max: {P}{max1}{W}')
print(f'8: {P}{c2}{W}, ({round(c2/chests*100, 2)}%), max: {P}{max2}{W}')
print(f'Ω: {P}{c3}{W}, ({round(c3/chests*100, 2)}%), max: {P}{max3}{W}')
print(f'Δ: {P}{c4}{W}, ({round(c4/chests*100, 2)}%), max: {P}{max4}{W}')
print(f'∑: {P}{chests}{W}')

sigma = 0
for i in plateau_15:
    t = [*map(int, i.split())]
    # if sum(t) > 0: print(t[3], sum(t) * 0.0425, '|', t[3] / sum(t), 0.0425)
    sigma += (t[3] - sum(t)*0.0425)**2
sigma = (sigma/len(plateau_15))**.5
# print(f'\nσ для 15* Плато = {round(sigma, 2)}')

print('\nЛокация    Полных Неполных Всего')
locs_data = dict(sorted(locs_data.items(), key=lambda x: sum(x[1])))
for location in locs_data:
    print(location, str(locs_data[location][0]).ljust(6), str(locs_data[location][1]).ljust(8), sum(locs_data[location]))
print(f'Типов: {str(len(locs_data)).ljust(3)} Всего запусков: {len(f)}')
