import time
import pyautogui

# pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
time.sleep(4)
x, y = pyautogui.position()
print("Posicao atual do mouse:")
print(x, y)
