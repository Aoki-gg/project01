import tkinter as tk
import app
import keyboard

# cria janela
janela = tk.Tk()
janela.title("BOT")
janela.geometry("300x100")

# botão
botao = tk.Button(janela, text="Start/Stop (F2)", command=lambda: app.run())
botao.pack()
keyboard.add_hotkey("f2", lambda: app.run())

# roda a interface
janela.mainloop()
