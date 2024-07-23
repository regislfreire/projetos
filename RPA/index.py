import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

# abrir o navegador
pyautogui.hotkey('win')
pyautogui.write('chrome')
pyautogui.press('enter')
#pyautogui.hotkey('alt', 'F4')

# inserir url
pyautogui.write('https://www.instagram.com/seasqqdqrf/')
pyautogui.press('enter')

# clicar no botão de seguir Point(x=1132, y=175)
pyautogui.click(1132, 175)
# clicar na opção de deixar de sehguir Point(x=872, y=736)
pyautogui.click(872, 736)
# fechar o navegador
pyautogui.hotkey('alt', 'F4')