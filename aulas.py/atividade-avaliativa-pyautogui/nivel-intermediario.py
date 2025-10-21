import pyautogui
import time

pyautogui.pause = 0.3
#print(pyautogui.KEYBOARD_KEYS)
pyautogui.press("win")

pyautogui.write("bloco de notas")
pyautogui.sleep(1)

pyautogui.press("enter")

pyautogui.sleep(1)

pyautogui.press("enter")

pyautogui.write("automatizar-com-pyautogui-talvez-seja-divertido.")
time.sleep(3)

pyautogui.click(x=1471, y=64)



pyautogui.press("win")

pyautogui.write("paint")

pyautogui.press("enter")

pyautogui.sleep(1)

pyautogui.press("enter")



time.sleep(3)
pyautogui.click(x=454, y=354)

pyautogui.dragRel(100, 0, duration=2)
pyautogui.dragRel(0, 100, duration=2)
pyautogui.dragRel(-100, 0, duration=2)
pyautogui.dragRel(0, -100, duration=2)

pyautogui.click(x=756, y=363)

time.sleep(1)
pyautogui.dragRel(100, 0, duration=2)
pyautogui.dragRel(0, 100, duration=2)
pyautogui.dragRel(-100, 0, duration=2)
pyautogui.dragRel(0, -100, duration=2)

pyautogui.click(x=1284, y=438)

time.sleep(1)

pyautogui.dragRel(100, 0, duration=2)
pyautogui.dragRel(0, 100, duration=2)
pyautogui.dragRel(-100, 0, duration=2)
pyautogui.dragRel(0, -100, duration=2)

 

