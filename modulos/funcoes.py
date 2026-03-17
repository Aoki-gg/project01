import pyautogui
from time import sleep
import cv2
import os
import sys

# Funçao para evitar problema com caminhos para acessar algo
def path(*paths):
    if getattr(sys, 'frozen', False):
        # executável criado pelo PyInstaller
        base_path = sys._MEIPASS
        
    else:
        # rodando no Python normal
        base_path = os.path.abspath(".")

    return os.path.join(base_path, *paths)


# Função que clica no centro de uma imagem
def click(imagem,typeclick):
    tipos_validos = {"1left", "2left", "right"}

    if typeclick not in tipos_validos:
        raise ValueError(
            "Escolha um segundo parametro válido: 1left,2left,right"
            )
    
    try:
        pos = pyautogui.locateCenterOnScreen(
            path("assets", "imagens", imagem),confidence=0.8
            )
        
        posicao_anterior=pyautogui.position()

        if pos:
            if typeclick == "1left":
                pyautogui.leftClick(pos)

            elif typeclick == "2left":
                pyautogui.doubleClick(pos)

            elif typeclick == "right":
                pyautogui.rightClick(pos)

        pyautogui.moveTo(posicao_anterior)
        sleep(0.5)
    
    except:
        pass


# Função que retorna as coordenadas ou None 
def img_find(imagem):
    try:
        verificação=pyautogui.locateOnScreen(
            path("assets", "imagens", imagem),confidence=0.8
            )
                        
    except:
        verificação=None
    
    return verificação
