# Pedi que o chatGPT criasse desafios para eu aprender a usar a biblioteca PyautoGUI. O nivel 0 são faceis e o nivel 5são dificeis.

import pyautogui
import pyperclip

# desafio 1, nivel 0
pyautogui.moveTo(x=100, y=100, duration=2)

# desafio 2, nivel 1
pyautogui.moveTo(500,420, duration=2)
pyautogui.click()
pyautogui.press('enter')
#pyperclip.copy('Olá, PyAutoGUI')
#pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.write('Olá, PyAutoGUI', interval=0.1)

Ol, PyAutoGUI