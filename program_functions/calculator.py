import tkinter as tk

def abrirCalculadora(janelaMenu):
    janelaMenu.withdraw()

    janelaCalculadora = tk.Toplevel()
    janelaCalculadora.title("MuTools - Calculadora")
    janelaCalculadora.geometry("900x450")

    textoBemVindo = tk.Label(janelaCalculadora, text="Calculadora:")
    textoBemVindo.grid(row=0, column=7, padx=10, pady=10)

    botao1 = tk.Button(janelaCalculadora, text="1")
    botao1.grid(row=2, column=3, padx=10, pady=10)

    botao2 = tk.Button(janelaCalculadora, text="2")
    botao2.grid(row=2, column=4, padx=10, pady=10)

    botao3 = tk.Button(janelaCalculadora, text="3")
    botao3.grid(row=2, column=5, padx=10, pady=10)

    botao4 = tk.Button(janelaCalculadora, text="4")
    botao4.grid(row=3, column=3, padx=10, pady=10)

    botao5 = tk.Button(janelaCalculadora, text="5")
    botao5.grid(row=3, column=4, padx=10, pady=10)

    botao6 = tk.Button(janelaCalculadora, text="6")
    botao6.grid(row=3, column=5, padx=10, pady=10)