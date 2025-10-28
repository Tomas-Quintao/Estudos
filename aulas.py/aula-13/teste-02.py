import pyautogui

import time 

time.sleep(5)

im1 = pyautogui.screenshot(region=(0,0,300,500))
im1.save("imagem2.png")
