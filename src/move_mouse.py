# -*- coding: utf-8 -*- 

import keyboard
import pyautogui

import random


class Key():
    """Classe que faz o tratamento da tecla pressionada
    
    metodos:
        get: recebe o callback da funcao 'on_press' e
        armazena nome e codigo da tecla pressionada.
            ** nao utiliza argumento
        clear: limpa as variaveis nome e codigo.
            ** necessario chamar a funcao
    atributos:
        name: letra ou caracter pressionado
        scan_code: codigo de varredura, posicao fisica da
        tecla no teclado.
    """
    
    def __init__(self) -> None:
        self.name = ''
        self.scancode = 0

    def get(self,event):
        self.name = event.name
        self.scan_code = event.scan_code

    def clear(self):
        self.name = ''
        self.scan_code = 0


x_size, y_size = pyautogui.size()

DURATION = 2.0
MARGIN = 10 # MAX: 50% da resolucao vertical (pixels)
SLEEP = 1.0
STOP_KEY = 'space'

tecla = Key()

# Move o cursor do mouse infinitamente, até que a tecla de stop seja pressionada
running = True
while running:

    if tecla.name:
        tecla.clear()

    # random para coordenadas aleatórias
    x = random.randint(MARGIN, x_size-MARGIN)
    y = random.randint(MARGIN, y_size-MARGIN)
    pyautogui.moveTo(x, y, DURATION)

    # Move o cursor do mouse para as coordenadas
    pyautogui.PAUSE = SLEEP

    keyboard.on_press(tecla.get)
    if tecla.name == STOP_KEY:
        running = False
