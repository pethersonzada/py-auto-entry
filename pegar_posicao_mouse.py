#Se ainda não tiver o pacote pyautogui instalado, vá no terminal da sua IDE e digite o comando "pip install pyautogui".

#pip install pyautogui

import time
import pyautogui

time.sleep(5) #Aguarda 5 segundos para iniciar o comando abaixo.
print(pyautogui.position()) #Pega a posição atual do mouse.

pyautogui.scroll(200)