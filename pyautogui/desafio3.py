#Desafio Nível 2: Capturar uma Captura de Tela e Salvar com Data e Hora
import pyautogui
import datetime

shot = pyautogui.screenshot('screenshot.png')
time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename=f' shot_{time}.png'
shot.save(filename) 