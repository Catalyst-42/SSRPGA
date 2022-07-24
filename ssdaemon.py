import datetime
import curses
import time
import os

os.system('''osascript -e 'tell application "Terminal" to set bounds of first window to {973, 769, 1200, 885}' ''')

text = ''
afk_time = 38_880 # 10h 48m
f = open('/Users/control/Desktop/Extension/SSRPGA/data.txt').read().splitlines()[-1][-19:]
timestamp = datetime.datetime.strptime(f, "%d.%m.%Y %H:%M:%S").timestamp()

s = curses.initscr(); sh, sw = s.getmaxyx()
curses.start_color(); curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK); curses.curs_set(0)

w = curses.newwin(sh, sw, 0, 0)
w.keypad(True); w.timeout(500)

def main():
    global timestamp, text

    trueexit = False
    while True:
        w.clear()
        if text == '':
            if time.time() - timestamp >= afk_time:
                curses.endwin()
                break
            
            delta = round(afk_time-(time.time()-timestamp))
            w.addstr(f'{datetime.timedelta(seconds=delta)} {round((time.time()-timestamp)/(afk_time)*100, 3):.3f}% ')
            w.addstr(f'{datetime.datetime.fromtimestamp(timestamp + afk_time).strftime("%d.%m %X")}\n', curses.color_pair(1))
        else: 
            w.addstr(f'Command: {text}')

        try: next_key = w.get_wch() 
        except: next_key = ''
        text += next_key

        if next_key == '\x7f': text = text[:-2]
        if next_key == '\x1b' or (next_key == '\n' and text[:-1] == 'exit'): curses.endwin(); trueexit = True; break
        if next_key == '\n': 
            if len(text) >= 2:
                command = text[:-1].split()
                if command[0] == 'timeout': 
                    w.timeout(int(float(command[1])*1000))
                if command[0] == 'ss':
                    curses.endwin()
                    break
            text = ''

    os.system('''osascript -e 'tell application "Terminal" to set bounds of first window to {847, 678, 1200, 811}' ''')
    if trueexit: return

    print('\033[31mRedirecting to ss\033[0m')
    os.system('cd /Users/control/Desktop/Extension/SSRPGA; python3 ssrpgauto.py -screen')
    timestamp = time.time()
    
    input()
    os.system('''osascript -e 'tell application "Terminal" to set bounds of first window to {973, 769, 1200, 885}' ''')
    text = ''
    main()

main()
