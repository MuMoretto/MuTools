import tkinter as tk

def abrirSobre(janelaMenu):
    janelaMenu.withdraw()

    janelaSobre = tk.Toplevel()
    janelaSobre.title("MuTools - Sobre")
    janelaSobre.geometry("900x450")
    janelaSobre.configure(bg="black")

    texto1 = tk.Label(janelaSobre, text="Criado por Murilo Moretto:", bg="lightgray")
    texto1.grid(row=0, column=0, padx=10, pady=10)

    janelaSobre.foto = tk.PhotoImage(file="assets/murilo.png")

    imagem = tk.Label(janelaSobre, image=janelaSobre.foto)
    imagem.grid(row=1, column=0, padx=10, pady=10)