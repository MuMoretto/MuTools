import tkinter as tk
from program_functions.menu_functions import abrirMenu

usuarios = [
    ("test", "123"),
    ("Murilo", "murilo2005")
]

janelaPrincipal = tk.Tk()
janelaPrincipal.title("MuTools - Versão Python")
janelaPrincipal.geometry("900x450")

textoBemVindo = tk.Label(janelaPrincipal, text="Bem-Vindo ao MuTools!")
textoBemVindo.grid(row=0, column=0, padx=10, pady=10)
textoUsuario = tk.Label(janelaPrincipal, text="Digite seu Usuário:")
textoUsuario.grid(row=1, column=0, padx=10, pady=10)
entradaUsuario = tk.Entry(janelaPrincipal)
entradaUsuario.grid(row=2, column=0, padx=10, pady=0)
textoSenha = tk.Label(janelaPrincipal, text="Digite sua Senha:")
textoSenha.grid(row=3, column=0, padx=10, pady=10)
entradaSenha = tk.Entry(janelaPrincipal)
entradaSenha.grid(row=4, column=0, padx=10, pady=0)

textoLogin = tk.Label(janelaPrincipal, text="")
textoLogin.grid(row=6, column=0, padx=10, pady=10)

def mostrarLogin():
    usuario = entradaUsuario.get()
    senha = entradaSenha.get()

    if (usuario, senha) in usuarios:
        textoLogin.config(text=f"Você logou como '{usuario}', com a senha '{senha}'")
        botaoContinuar.grid(row=7, column=0, padx=10, pady=10)
    else:
        textoLogin.config(text="Usuário ou senha incorretos! Tente novamente...")

botaoLogar = tk.Button(janelaPrincipal, text="Logar", command=mostrarLogin)
botaoLogar.grid(row=5, column=0, padx=10, pady=20)

botaoContinuar = tk.Button(janelaPrincipal, text="Continuar", command=lambda: abrirMenu(janelaPrincipal))               # Criei o botão aqui e ele só aparece depois da exibição da mensagem de login... O mesmo foi chamado na função "mostrarLogin".

janelaPrincipal.mainloop()