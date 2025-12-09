import tkinter as tk
from program_functions.calculator import abrirCalculadora

def abrirMenu(janelaPrincipal):
    janelaPrincipal.withdraw()

    janelaMenu = tk.Toplevel()
    janelaMenu.title("MuTools - Menu Inicial")
    janelaMenu.geometry("900x450")

    textoEscolhaOpcao = tk.Label(janelaMenu, text="Escolha uma opção abaixo:")
    textoEscolhaOpcao.grid(row=0, column=0, padx=10, pady=10)

    botaoCalculadora = tk.Button(janelaMenu, text="Calculadora", command=lambda: abrirCalculadora(janelaMenu))
    botaoCalculadora.grid(row=1, column=0, padx=10, pady=10)

    botaoSobre = tk.Button(janelaMenu, text="Sobre")
    botaoSobre.grid(row=2, column=0, padx=10, pady=10)