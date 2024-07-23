'import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.click()
pyautogui.moveTo(200, 200, duration=0.5)