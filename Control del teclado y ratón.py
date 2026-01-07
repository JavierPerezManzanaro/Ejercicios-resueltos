
# https://orteil.dashnet.org/cookieclicker/

# sacado de aquí: https://www.youtube.com/shorts/hs5a4FvnWd4


# source venv-ejercicios_resueltos/bin/activate
# pip install pynput

from pynput.keyboard import Controller as KC
from pynput.mouse import Button, Controller as MC, Button

import time


keyboard = KC()
mouse = MC()



def acciones():
    """Hace clic izquierdo cada cierto tiempo"""
    while True:
        mouse.click(Button.left, 1) # clic izquierdo
        time.sleep(1)

"""
Escribe un caracter en concreto cada cierto tiempo
def acciones():
    while True:
        keyboard.press ('a') # presiona la tecla 'a'
        keyboard.release('a') # suelta la tecla 'a'
        time.sleep(5)
"""
        
        
acciones()