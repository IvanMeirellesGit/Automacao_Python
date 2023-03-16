import time

import pyautogui


def copiar_Texto():
    p.keyDown('ctrl')
    p.press('c')
    p.keyUp('ctrl')


def colar_Texto():
    p.keyDown('ctrl')
    p.press('v')
    p.keyUp('ctrl')


def altTab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')


def criar_Pastas():
    p.keyDown('Ctrl')
    p.keyDown('Shift')
    p.press('n')
    p.keyUp('Ctrl')
    p.keyUp('Shift')
    time.sleep(0.2)
    p.press('Enter')
    time.sleep(0.2)


def iniciar_Explorador():
    p.press('win')
    time.sleep(0.2)
    p.write('Explorador de arquivos')
    time.sleep(0.5)
    p.press('enter')
    time.sleep(0.5)


p = pyautogui

# # Para abir a pasta da pos graduação
altTab()

iniciar_Explorador()

p.moveTo(710, 329)
time.sleep(0.5)
p.doubleClick()
time.sleep(0.3)
p.write('b')
p.press('enter')
time.sleep(0.2)
p.write('e')
p.press('enter')
time.sleep(0.2)
p.write('p')
p.press('enter')
time.sleep(0.2)
p.press(['down', 'down', 'down'])
p.press('enter')

criar_Pastas()
altTab()


p.moveTo(188, 200)
time.sleep(0.2)
p.tripleClick()
copiar_Texto()

altTab()
time.sleep(0.3)
p.rightClick(364, 326)
p.press('F2')
colar_Texto()
p.press('Enter')
