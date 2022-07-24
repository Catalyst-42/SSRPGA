from sys import argv

W = '\033[0m'
B = '\033[30m'
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
M = '\033[35m'
C = '\033[36m'
help_line = f'''Использование:
{R}-l{W} location выход на определенную локацию
   {R}1{W} - Плато {R}2{W} - Каньон {R}3{W} - Пещеры {R}4{W} - Грибы
   {R}5{W} - Залы  {R}6{W} - Шахта  {R}7{W} - Хребет {R}8{W} - Храм
{R}-e{W} exit завершить без выхода из игры
{R}-i{W} intro пропустить вступление
{R}-c{W} chest пропустить сбор сундуков
{R}-s{W} shop пропустить Грибную лавку'''

if '-help' in argv:
    print(help_line)
    exit()

print(f'{Y}Loading ssrpgauto:')
import time
import os

if '-screen' not in argv:
    os.system('''osascript -e 'tell application "Terminal" to set bounds of first window to {850, 400, 1203, 533}'; clear''')

print('Vision', end=' ', flush=True); import vision; print('loaded')
print('pyAutogui', end=' ', flush=True); import pyautogui; print('loaded')
pyautogui.PAUSE = 0
print('pyTesseract', end=' ', flush=True); import pytesseract; print(f'loaded{W}')
from pynput.mouse import Button, Controller as MC
mouse = MC()

if '-i' not in argv: 
    print(f'{Y}\nLaunching SS...{W}')
    os.system('open /Users/control/Desktop/Extension/SSRPGA/ss.app')

def flooder(clicks):
    for _ in range(clicks):
        time.sleep(0.3)
        mouse.click(Button.left)

def buy():
    time.sleep(0.5)
    set_position(1188, 443)
    click(Button.left)

def set_position(x, y, sleep=.3):
    mouse.position = (x, y)
    time.sleep(sleep)

def click(button, times=1, sleep=.3):
    mouse.click(button, times)
    time.sleep(sleep)

def hold(hold_time=1, sleep=.3):
    mouse.press(Button.left)
    time.sleep(hold_time)
    mouse.release(Button.left)
    time.sleep(sleep)
    
# region откытие дата файла и дампинг старых данных
line_old = open('data.txt').readlines()[-1]

resources_old = line_old[0:120].translate({ord(_): None for _ in '+-=|,'})
resources_old = [int(_) for _ in resources_old.split()]

chests_old = [*map(int, line_old[122:138].split())]
chests = [0]*4
# endregion

# region нажатие на старт
if '-i' not in argv:
    time.sleep(1.5)
    while 1:
        if pyautogui.locateOnScreen('p1.png'): break
        else: time.sleep(2)
click(Button.left)
set_position(329, 544)
click(Button.left)
# endregion

# region смотр полученных сундуков
if '-c' not in argv:
    while 1:
        if pyautogui.locateOnScreen('p2.png'): break
        else: time.sleep(1.5)

    pyautogui.screenshot('chests.png', region=(360, 72, 720, 756))
    pyautogui.screenshot('screenshot.png', region=(420, 432, 600, 36)) # small window
    chests_vision = vision.image_to_text('screenshot.png')

    if not chests_vision or chests_vision[0][0][0] not in 'Xx×':
        pyautogui.screenshot('screenshot.png', region=(420, 396, 600, 36)) # long window
        chests_vision = vision.image_to_text('screenshot.png')
    
    print(f"{Y}{' '.join([_[0] for _ in chests_vision])}{W}")
    chest = index = 0
    while chest < 3:
        if pyautogui.locateOnScreen(('c1.png', 'c2.png', 'c3.png')[chest]):
            chests[chest] = int(chests_vision[index][0].translate({ord(_): None for _ in 'Xx×'}))
            index += 1
        chest += 1

    if len(chests_vision) - 1 == index:
        chests[chest] = int(chests_vision[index][0][1:])
    print(f'{Y}{chests}{W}')
# endregion

# region забор лута
if '-c' not in argv:
    set_position(190, 680)
    click(Button.left)
    # переход на окно лута
    set_position(190, 490)
    click(Button.left, 1, 1)
    # листаю вверх на всякий
    set_position(1404, 270)
    hold()
    # нажимаю на сундук
    set_position(490, 340)
    click(Button.left)
    # открываю сундуки
    set_position(590, 490)
    click(Button.left)
    # ждем все сундуки
    set_position(335, 685)
    while pyautogui.locateOnScreen('p3.png'): flooder(20)
    set_position(190, 115)
    click(Button.left)
# endregion

# region магазин
# открываю окно вида и листаю на магазин
# листаю на магаз
set_position(1290, 485)
hold()

# проверка на пустоту магаза
meta = []
img = pyautogui.screenshot(region=(875, 430, 459, 36))
text = pytesseract.image_to_string(img, config=r'--oem 3 --psm 6', lang='rus').strip()
if text != '' and '-s' not in argv:
    meta.append(f'Лавка [{G}✓{W}]')
    set_position(650, 450)
    click(Button.left)

    # покупаю все в магазине
    for pos in ((670, 160), (1090, 160), (670, 376), (1090, 376), (670, 592), (1090, 595)):
        mouse.position = pos
        time.sleep(0.5)
        mouse.click(Button.left)
        buy()

    # сундуки магазина
    for pos in ((607, 808), (891, 823), (1168, 813)):
        time.sleep(0.5)
        mouse.position = pos
        time.sleep(0.5)
        mouse.click(Button.left)
        buy()
        mouse.position = (336, 687)
        flooder(9)

    # выходим в меню локаций
    set_position(207, 132)
    click(Button.left)
else: meta.append(f'Лавка [{R}x{W}]')
# endregion

# region hotspring shop
meta.append(f'Ключ [{G}✓{W}]')
set_position(975, 240)
click(Button.left, 1, 3)
while 1:
    if pyautogui.locateOnScreen('p4.png'): break
    else: time.sleep(1.5)
set_position(670, 415)
click(Button.left)
# endregion

# region счет ресурсов
time.sleep(1)
resources = []

pyautogui.screenshot('screenshot.png', region=(160, 252, 200, 252))
for res in vision.image_to_text('screenshot.png'): resources.append(res[0])
meta.append(f"{Y}{' '.join(resources)}{W}") # Выыод считанного текста

resources = [int(_) for _ in resources]
time.sleep(0.5)

set_position(195, 130)
click(Button.left)
# endregion

# region выход - определение выхода
# 0 - Плато 1 - Каньон 2 - Пещеры 3 - Грибы
# 4 - Залы  5 - Шахта  6 - Хребет 7 - Храм
if '-l' in argv: outloc = int(argv[argv.index('-l')+1]) - 1
else: outloc = 0
match outloc:
    case 0: # ВЫХОД на плато
        loc = ('15*', 'Плато')
        # крутим вниз
        set_position(1290, 880)
        hold()
        # открываю диза
        set_position(970, 810)
        click(Button.left)

    case 1: # ВЫХОД на каньон
        loc = ('15*', 'Каньон')
        # крутим вниз
        set_position(1290, 880)
        hold()
        # открываю каньон
        set_position(970, 590)
        click(Button.left)

    case 2: # ВЫХОД на пещеры
        loc = ('15*', 'Пещеры')
        # крутим на пещеры
        set_position(1290, 880)
        hold()
        # открываем пещеры
        set_position(970, 380)

    case 3: # ВЫХОД на грибы
        loc = ('15*', 'Грибы')
        set_position(970, 670)

    case 4: # ВЫХОД на залы
        loc = ('15*', 'Залы')
        # крутим вниз
        set_position(1290, 310)
        hold()
        # открываю карточку
        set_position(970, 380)
        click(Button.left)

    case 5: # ВЫХОД на шахты
        loc = ('15*', 'Шахты')
        # крутим на шахты
        set_position(1290, 55)
        hold()
        # открываем шахты
        time.sleep(0.5)
        set_position(970, 845)

    case 6: # ВЫХОД на хребет
        loc = ('15*', 'Хребет')
        # крутим на хребет
        set_position(1290, 55)
        hold()
        # открываем хребет
        time.sleep(0.5)
        set_position(970, 635)

    case 7: # ВЫХОД на храм
        loc = ('15*', 'Храм')
        # крутим на храм
        set_position(1290, 55)
        hold()
        # открываем храм
        time.sleep(0.5)
        set_position(970, 200)
# endregion

# region ставим выход
meta.append(f'{loc[1]} {loc[0]}')
click(Button.left)
set_position(1065, 765)
click(Button.left)
if '-e' not in argv: # выход
    set_position(324, 705, 3.5)
    click(Button.left, 1, 0.1)
# endregion

# region дата запись
if '-c' not in argv:
    file = open('data.txt', 'a')
    for i in range(len(resources) - 1): 
        file.write(f'{resources[i]:,}'.ljust(14))

        if resources_old[i] < resources[i]: file.write('+') 
        elif resources_old[i] > resources[i]: file.write('-')
        else: file.write('=')
        
        file.write('  | ')
    file.write(str(resources[-1]).ljust(5) + ' | ')

    for i in chests: file.write(str(i).ljust(3) + ' ')
    file.write('| ' + (loc[0]).ljust(4) + loc[1].ljust(6) + ' | ' + time.strftime('%d.%m.%Y %H:%M:%S') + '\n')
    file.close()
    # endregion

    # region вывод красивого лога в консоль
    def gain(i):
        if resources[i] < resources_old[i]: return f'{R}{resources[i] - resources_old[i]:,}{W}'
        elif resources[i] > resources_old[i]: return f'{G}+{resources[i] - resources_old[i]:,}{W}'
        else: return f'{Y}{W}'

    def chest_dynamic(chest_index):
        if (chests[chest_index] > chests_old[chest_index] and chest_index != -1) or (
            sum(chests) > sum(chests_old) and chest_index == -1):
            return f'{G}↑{W}'
        elif (chests[chest_index] == chests_old[chest_index] and chest_index != -1) or (
            sum(chests) == sum(chests_old) and chest_index == -1):
            return f'{Y}-{W}'
        else: 
            return f'{R}↓{W}'

    print(meta[2])
    print("   Добыча   |        Ресурсы        |   Регион   ")
    for data in (('=', sum(chests), chest_dynamic(-1), 'o', f'{resources[0]:,}', gain(0), meta[3]), 
                ('o', chests[0],   chest_dynamic(0),  '/', f'{resources[1]:,}', gain(1), ''),
                ('8', chests[1],   chest_dynamic(1),  '≈', f'{resources[2]:,}', gain(2), f'{M}♦{W} {resources[6]:,} {gain(6)}'),
                ('Ω', chests[2],   chest_dynamic(2),  ':', f'{resources[3]:,}', gain(3), f'* {resources[5]:,}'),
                ('Δ', chests[3],   chest_dynamic(3),  '@', f'{resources[4]:,}', gain(4), meta[0])):
        print(f'{data[0]} {str(data[1]).ljust(7)} {data[2]} | {data[3]} {data[4].ljust(10)} {data[5].ljust(17)} | {data[6]}')
    # endregion
# endregion
