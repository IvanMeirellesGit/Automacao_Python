import time
import pyautogui


p = pyautogui


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
    time.sleep(0.2)
    p.press('enter')
    time.sleep(0.5)


def iniciar_Edge():

    p.press('win')
    time.sleep(0.1)
    p.write('http://www.descomplica.com.br')
    time.sleep(0.1)
    p.press('Enter')
    time.sleep(30)


def iniciar_Notas():
    p.press('win')
    time.sleep(0.2)
    p.write('Bloco de notas')
    time.sleep(0.2)
    p.press('Enter')

    # Inicia o programa


# iniciar_Edge()
altTab()

# Para selecionar o texto das disciplinas
p.click(41, 269)
time.sleep(2)
p.moveTo(1849, 202)
time.sleep(0.1)
p.drag(0, 530, 0.8)
time.sleep(0.3)
p.moveTo(418, 222)
time.sleep(0.1)
p.drag(xOffset=600, yOffset=700, duration=0.8)
time.sleep(0.5)

# Para copiar o texto selecionado
copiar_Texto()
time.sleep(0.5)
# Abrir Bloco de notas
iniciar_Notas()
time.sleep(0.5)
# Colar texto copiado
colar_Texto()
time.sleep(0.5)
# # Para abir a pasta da pos graduação
iniciar_Explorador()
time.sleep(0.5)

p.moveTo(710, 329)
time.sleep(0.2)
p.doubleClick()
time.sleep(0.3)
p.write('b')
p.press('enter')
time.sleep(0.1)
p.write('e')
p.press('enter')
time.sleep(0.1)
p.write('p')
p.press('enter')
time.sleep(0.1)
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
