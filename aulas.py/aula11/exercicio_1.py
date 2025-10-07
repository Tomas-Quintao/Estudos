import pyautogui
import time

pyautogui.pause = 0.3
#print(pyautogui.KEYBOARD_KEYS)
pyautogui.press("win")

pyautogui.write("bloco de notas")

pyautogui.press("enter")

pyautogui.sleep(1)

pyautogui.press("enter")

pyautogui.write("Macho-Freitas")

pyautogui.sleep(1)

pyautogui.hotkey("Ctrl", "w")
pyautogui.sleep(1)
pyautogui.press("n")





