# -*- coding: utf-8 -*- 

import keyboard
import pyautogui

from move_mouse import Key

key = Key()

SLEEP = 0.1 # click a cada 100 ms (segundos)
STOP_KEY = 'space'

running = True
while running:

    if key.name:
        key.clear()

    # click automatico com intervalo.
    pyautogui.leftClick(interval=SLEEP)

    keyboard.on_press(key.get)
    if key.name == STOP_KEY:
        running = False
