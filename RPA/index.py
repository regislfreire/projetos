import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.7
pyautogui.FAILSAFE = True

# criando o dataframe com os contatos
contatos = pd.read_csv('contatos.csv')

# abrir o navegador
pyautogui.hotkey('win')
pyautogui.write('chrome')
pyautogui.press('enter')
#pyautogui.hotkey('alt', 'F4')

for linha in contatos.index: # inserir url
    url=str(contatos.loc[linha, 'url'])
    pyautogui.write(url)
    pyautogui.press('enter')
    pyautogui.moveTo(362,146)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('space')
    pyautogui.click(x=592, y=63)
pyautogui.hotkey('alt', 'F4')