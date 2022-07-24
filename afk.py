import os
import time
from pynput import keyboard
from pynput.mouse import Button, Controller as MC
from pynput.keyboard import Key, Controller as KC

loop = 0
mouse = MC()
keyboard = KC()
os.system('clear')

def position(x, y, sleep=.5):
    mouse.position = (x, y)
    time.sleep(sleep)

def click(button, times=1, sleep=.5):
    mouse.click(button, times)
    time.sleep(sleep) 

while 1:
    print(f'L{loop}')
    loop+=1
    time.sleep(95)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(.5)
    keyboard.press('l')
    keyboard.release('l')
    time.sleep(.5)
    position(970,200)
    click(Button.left)
    position(790,780)
    click(Button.left)
