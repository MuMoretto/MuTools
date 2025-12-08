import tkinter as tk

janelaPrincipal = tk.Tk()
janelaPrincipal.title("MuTools - Versão Python")
janelaPrincipal.geometry("1400x700")

textoBemVindo = tk.Label(janelaPrincipal, text="Bem-Vindo ao MuTools!")
textoBemVindo.grid()
textoUsuario = tk.Label(janelaPrincipal, text="Digite seu Usuário:")
textoUsuario.grid()
entradaUsuario = tk.Entry(janelaPrincipal)
entradaUsuario.grid()
textoSenha = tk.Label(janelaPrincipal, text="Digite sua Senha:")
textoSenha.grid()
entradaSenha = tk.Entry(janelaPrincipal)
entradaSenha.grid()

textoLogin = tk.Label(janelaPrincipal, text="")
textoLogin.grid()

def mostrarLogin():
    avisoUsuario = entradaUsuario.get()
    avisoSenha = entradaSenha.get()
    texto = tk.Label(janelaPrincipal, text=f"Você logou como '{avisoUsuario}', com a senha: '{avisoSenha}'...")
    texto.grid()
    botaoContinuar.grid()

botaoLogar = tk.Button(janelaPrincipal, text="Logar", command=mostrarLogin)
botaoLogar.grid()

botaoContinuar = tk.Button(janelaPrincipal, text="Continuar")               # Criei o botão aqui e ele só aparece depois da exibição da mensagem de login... O mesmo foi chamado na função "mostrarLogin".

janelaPrincipal.mainloop()