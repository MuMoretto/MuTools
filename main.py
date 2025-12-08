import tkinter as tk

janelaPrincipal = tk.Tk()
janelaPrincipal.title("MuTools - Versão Python")
janelaPrincipal.geometry("1400x700")

textoBemVindo = tk.Label(janelaPrincipal, text="Bem-Vindo ao MuTools!")
textoBemVindo.pack()
textoUsuario = tk.Label(janelaPrincipal, text="Digite seu Usuário:")
textoUsuario.pack()
entradaUsuario = tk.Entry(janelaPrincipal)
entradaUsuario.pack()
textoSenha = tk.Label(janelaPrincipal, text="Digite sua Senha:")
textoSenha.pack()
entradaSenha = tk.Entry(janelaPrincipal)
entradaSenha.pack()

textoLogin = tk.Label(janelaPrincipal, text="")
textoLogin.pack()

def mostrarLogin():
    avisoUsuario = entradaUsuario.get()
    avisoSenha = entradaSenha.get()
    texto = tk.Label(janelaPrincipal, text=f"Você logou como '{avisoUsuario}', com a senha: '{avisoSenha}'...")
    texto.pack()
    botaoContinuar.pack()

botaoLogar = tk.Button(janelaPrincipal, text="Logar", command=mostrarLogin)
botaoLogar.pack()

botaoContinuar = tk.Button(janelaPrincipal, text="Continuar")               # Criei o botão aqui e ele só aparece depois da exibição da mensagem de login... O mesmo foi chamado na função "mostrarLogin".

janelaPrincipal.mainloop()