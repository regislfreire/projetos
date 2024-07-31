# Arquivo auxiliar
import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5 # Definindo que para casa de comando o PyAutoGUI irá aguardar 1 segundo entre cada comando

# abrindo bloco de notas
time.sleep(2)
pyautogui.press('win')
pyautogui.write('notepad', interval=0.3)
pyautogui.press('enter')

pyautogui.moveTo(x=300, y=300, duration=2)
pyautogui.click()

#for i in range():
pyautogui.hotkey('alt', '0233')
