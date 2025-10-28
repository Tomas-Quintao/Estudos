import pyautogui

import time 

print("passe o mause sobre o canto superior esquerdo da janela")
time.sleep(5)
p_inicial = (pyautogui.position())
print("canto superior esquerdo:",p_inicial)
time.sleep(5)

print("agora passe o mouse sobre o canto inferior direito da janela")
time.sleep(5)
p_final = (pyautogui.position())
print("canto inferior direito:",p_final)

largura = p_final.x -x- p_inicial.x
altura = p_final.y -y- p_inicial.y
print(f"area da janela: x={p_inicial.x}, y={p_inicial.y},largura = {largura},altura = {altura}")

