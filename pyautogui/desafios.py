import pyautogui
import pyperclip
import time

# Pedi que o chatGPT criasse desafios para eu aprender a usar a biblioteca PyautoGUI. O nivel 0 são faceis e o nivel 5são dificeis.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5 # Definindo que para casa de comando o PyAutoGUI irá aguardar 1 segundo entre cada comando

# abrindo bloco de notas
time.sleep(2)
pyautogui.press('win')
pyautogui.write('notepad', interval=0.3)
pyautogui.press('enter')

# desafio 1, nivel 0 (mover o cursor para o canto superior esquerdo)
pyautogui.moveTo(x=300, y=300, duration=2)
pyautogui.click()

# desafio 2, nivel 1 (escrever o texto "Olá, PyAutoGUI")
#pyautogui.moveTo(x=100, y=100, duration=2)
#pyautogui.write('Olá, PyAutoGUI', interval=0.5)
pyperclip.copy('Olá, PyAutoGUI')
pyautogui.hotkey('ctrl', 'v')

# Fechando o Bloco de Notas
time.sleep(5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
pyautogui.hotkey('alt', 'f4')