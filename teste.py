import os
import time
import pyautogui

# Diretório onde os arquivos PJC foram extraídos
# pasta_arquivos = "C:/Users/anacb/Documents/py 2/ARQUIVOS PJE-C.rar"  # Use barras normais

# # Lista de arquivos PJC
# arquivos = [f for f in os.listdir(pasta_arquivos) if f.endswith('.pjc')]

# # Abrir o PJe-Calc
# os.startfile("caminho/para/o/PJe-Calc.exe")  # Use barras normais
# time.sleep(10)  # Esperar o PJe-Calc abrir

# for arquivo in arquivos:
    # Simular a importação de cada arquivo PJC
import pyautogui
import time

for i in range(50):
    pyautogui.click(x=1800, y=0)  # Coordenadas do botão 'Importar'
    time.sleep(2)

    pyautogui.doubleClick(x=0, y=650)  # Coordenadas do botão 'Importar'
    time.sleep(2)

    pyautogui.click(x=930, y=570)  # Coordenadas do botão 'Importar'
    time.sleep(1)

    if i > 0:
         pyautogui.click(x=930, y=550) 
         time.sleep(1) 

    pyautogui.click(x=930, y=540)  # Coordenadas do botão 'Importar'
    time.sleep(2)

    pyautogui.click(x=930, y=520)  # Coordenadas do botão 'Importar'
    time.sleep(1)

    pyautogui.click(x=300, y=190)  # Coordenadas do botão 'Importar'
    time.sleep(1)

    # Coordenada y aumentada em 20 a cada iteração
    # pyautogui.doubleClick(x=300, y=160)  # Coordenadas do botão 'Importar'
    # time.sleep(2)

    # pyautogui.doubleClick(x=300, y=160 + i * 20)  # Coordenadas do botão 'Importar'
    # time.sleep(2)

    pyautogui.doubleClick(x=300, y=160 + i*25)  # Coordenadas do botão 'Importar'
    time.sleep(1)

    pyautogui.click(x=300, y=320)  # Coordenadas do botão 'Importar'
    time.sleep(1)

    pyautogui.click(x=1800, y=0)  # Coordenadas do botão 'Importar'



