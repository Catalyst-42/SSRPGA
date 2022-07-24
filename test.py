#!/bin/env python3
from operator import index
import os
import time
import vision
import pyautogui
import pytesseract
from sys import argv
from pynput.mouse import Button, Controller as MC

os.chdir('/Users/control/Desktop/Extension/SSRPGA/')
print(os.system('echo | pwd'))

# region INIT
mouse = MC()
config = r'--oem 3 --psm 6'
meta = []

mouse = MC()
config = r''#'--oem 3 --psm 6'
def position(x, y, sleep=.4):
    mouse.position = (x, y)
    time.sleep(sleep)
# endregion

if '-l' in argv: 
    print(argv)
    print(argv[argv.index('-l')+1])

os.system("clear")

# region RECOGNITION
# time.sleep(1)
# image = pyautogui.screenshot('chests.png', region=(360, 72, 720, 756))
# img = pyautogui.screenshot('screenshot.png', region=(0, 0, 1440, 36))
# resources = ''
# for i in vision.image_to_text('screenshot.png'): resources += i[0] + ' '
# print('\033[33m', resources, '\033[0m\n')

# resources = resources.replace(', ', ',')
# resources = resources.replace('Ac', '=')
# if resources[0] == '0': resources = resources[1:]
# resources = resources.translate({ord(i): None for i in '+,o-—_/`°>=:.@©&•O~'})

# print('')
# resources = resources.split()
# for i in range(len(resources)): resources[i] = int(resources[i])
# print('Ресурсы')
# for i in range(5):
#     print((['o', '/', '≈', ':', '@'][i] + ' ' + str(pn(resources[i]))).ljust(15))
# time.sleep(0.5)
# endregion

# region OUT TABLE
# W = '\033[0m'
# B = '\033[30m'
# R = '\033[31m'
# G = '\033[32m'
# Y = '\033[33m'
# M = '\033[35m'
# C = '\033[36m'
# '''
#    Добыча   |        Ресурсы        |   Регион   
# = 313       | o 908,619     +2,586  | Плато 15*
# o 0         | / 25,905              | 
# 8 164       | ≈ 6,672,867           | ♦ 35 +1
# Ω 129       | : 76,251      -40     | * 12,577 
# Δ 20        | @ 7,269,461   -77,618 | Ганс [✓]
# '''

# # Самое дорогое
# '''   Добыча   |        Ресурсы        |   Регион  
# = 204 {G}▃{G}▄{G}▅{G}▆{G}▇{W} | o 221,087     {G}+130{W}    | Пещеры 15*
# o 148 {G}▁{G}▂{G}▃{G}▇{R}▆{W} | / 24,613      {W}{W}        |
# 8 16  {Y}▆{R}▁{G}▃{R}▂{R}▁{W} | ≈ 471,861     {R}-90{W}     | {M}♦{W} 35 {G}+1{W}
# Ω 38  {Y}▆{Y}▆{R}▄{Y}▄{Y}▄{W} | : 60,469      {G}+1,711{W}  | * 12,577
# Δ 2   {Y}▃{Y}▃{Y}▃{R}▁{G}▂{W} | @ 8,118,096   {R}-77,618{W} | Лавка [{G}✓{W}]
# '''

# print(f'''   Добыча   |        Ресурсы        |   Регион  
# = 204      {R}↓{W}| o 221,087     {G}+130{W}    | Пещеры 15*
# o 148      {G}↑{W}| / 24,613      {Y}{W}        |
# 8 16       {R}↓{W}| ≈ 471,861     {R}-90{W}     | {M}♦{W} 35 {G}+1{W}
# Ω 38       {Y}-{W}| : 60,469      {G}+1,711{W}  | * 12,577
# Δ 2        {G}↑{W}| @ 8,118,096   {R}-77,618{W} | Лавка [{G}✓{W}]
# ''')

# chests_old = [0, 300, 308, 1]
# chests = [148, 16, 308, 2]

# meta = ['Ганс [\033[32m✓\033[0m]', 'Ключ [\033[31mx\033[0m]', f'{Y}X232 X155 X13\n1062904 27499 6673887 73765 6896229 13752 144{W}','Пещеры 15*']
# resources_old = [220957, 24613, 471951, 58758, 8195714, 12500, 100, 156, 34, 55, 5, '15', 'Шахты']
# resources = [221087, 24613, 471861, 60469, 8318096, 12500, 103]

# def chest_dynamic(chest_index):
#     if (chests[chest_index] > chests_old[chest_index] and chest_index != -1) or (
#         sum(chests) > sum(chests_old) and chest_index == -1):
#         return f'{G}↑{W}'
#     elif (chests[chest_index] < chests_old[chest_index] and chest_index != -1) or (
#         sum(chests) < sum(chests_old) and chest_index == -1):
#         return f'{R}↓{W}'
#     else: 
#         return f'{Y}-{W}'

# def gain(i):
#     if resources[i] - resources_old[i] < 0: return f'\033[31m{resources[i] - resources_old[i]:,}\033[0m'
#     elif resources[i] - resources_old[i] > 0: return f'\033[32m+{resources[i] - resources_old[i]:,}\033[0m'
#     else: return f'{Y}{W}'

# # os.system('osascript -e ' + "'tell application " + '"Terminal"' + " to set bounds of front window to {850, 500, 1203, 633}'")
# print(meta[2])
# print("   Добыча   |        Ресурсы        |   Регион   ")
# for data in (('=', sum(chests), chest_dynamic(-1), 'o', f'{resources[0]:,}', gain(0), meta[3]), 
#              ('o', chests[0],   chest_dynamic(0),  '/', f'{resources[1]:,}', gain(1), ''),
#              ('8', chests[1],   chest_dynamic(1),  '≈', f'{resources[2]:,}', gain(2), f'{M}♦{W} {resources[6]:,} {gain(6)}'),
#              ('Ω', chests[2],   chest_dynamic(2),  ':', f'{resources[3]:,}', gain(3), f'* {resources[5]:,}'),
#              ('Δ', chests[3],   chest_dynamic(3),  '@', f'{resources[4]:,}', gain(4), meta[0])):
#     print(f'{data[0]} {str(data[1]).ljust(7)} {data[2]} | {data[3]} {data[4].ljust(10)} {data[5].ljust(17)} | {data[6]}')
# endregion

# region Resources v2
# img = pyautogui.screenshot('screenshot.png', region=(160, 252, 200, 252))
# resources = []
# for res in vision.image_to_text('screenshot.png'): resources.append(res[0])

# for i, res in enumerate(["o", "/", "≈", ":", "@", "♦", "*"]):
#     print(res, resources[i])

# endregion        

# region Chests 
'''
Small
(420, 432) (1019, 432) 
(420, 467) (1019, 467)

Big
(420, 396) (1019, 396)
(420, 431) (1019, 431)
'''

file = open('data.txt', 'r+')
line_old = file.readlines()[-1]
resources_old = line_old[0:120]
resources_old = resources_old.translate({ord(i): None for i in '+-=|,'})
resources_old = [int(x) for x in resources_old.split()]
chests_old = [*map(int, line_old[122:138].split())]

chests = [0]*4

time.sleep(2)
while 1:
    if pyautogui.locateOnScreen('p2.png'): break
    else: time.sleep(2)
image = pyautogui.screenshot('chests.png', region=(360, 72, 720, 756))

image = pyautogui.screenshot('screenshot.png', region=(420, 432, 600, 36)) # small window
chests_vision = vision.image_to_text('screenshot.png')
print(f'{chests_vision=}')

if not chests_vision or chests_vision[0][0][0] not in 'Xx×':
    image = pyautogui.screenshot('screenshot.png', region=(420, 396, 600, 36)) # long window
    chests_vision = vision.image_to_text('screenshot.png')
    print(f'{chests_vision=}')

chest = index = 0
while chest < 3:
    if pyautogui.locateOnScreen(('c1.png', 'c2.png', 'c3.png')[chest]): 
        chests[chest] = int(chests_vision[index][0][1:])
        index += 1
    chest += 1

if len(chests_vision) - 1 == index:
    chests[chest] = int(chests_vision[index][0][1:])

print('>>>', chests, '<<<')
os.system('say done')
# endregion
