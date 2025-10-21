import pyautogui
import time

pyautogui.pause = 0.3
#print(pyautogui.KEYBOARD_KEYS)
pyautogui.press("win")


pyautogui.write("bloco de notas")
pyautogui.sleep(2)

pyautogui.press("enter")

pyautogui.sleep(1)

pyautogui.press("enter")

pyautogui.write("\nautomatizar com pyautogui talvez seja divertido.",interval=0.2)
pyautogui.write("\nautomatizar com pyautogui talvez seja divertido.",interval=0.2)
pyautogui.write("\nautomatizar com pyautogui talvez seja divertido.",interval=0.2)

time.sleep(3)

pyautogui.click(x=77, y=84)
time.sleep(1)

pyautogui.click(x=118, y=321)
pyautogui.sleep(2)
pyautogui.write("anotacao.txt")
pyautogui.press("enter")





