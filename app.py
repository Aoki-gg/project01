from modulos import funcoes as f
from time import sleep
import threading

executando=False

# Função necessaria para executar o programa principal
def run():
    global executando
    
    if not executando:
        executando = True
        threading.Thread(target=aplication, daemon=True).start()
   
    else:
        executando= False


# Programa principal
def aplication():
    global executando 
    
    while executando:
        f.click("imagem1.png","1left")
        sleep(0.5)
        f.click("imagem2.png","1left")
        sleep(0.5)
        f.click("imagem3.png","2left")
        sleep(0.5)
