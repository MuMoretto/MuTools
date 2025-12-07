import tkinter as tk

accounts = [
    ("MuMoretto", "Murilo2005#"),
    ("Luna", "Luna123")
]

loginWindow = tk.Tk()
loginWindow.title("MuTools - Login")
loginWindow.geometry("1400x700")            # Horizontal X Vertical
login_window = tk.Frame(loginWindow)
login_window.pack()

tk.Label(login_window, text="Usuário").pack()
user_entry = tk.Entry(login_window)
user_entry.pack()

tk.Label(login_window, text="Senha").pack()
password_entry = tk.Entry(login_window)
password_entry.pack()

def verify_account():
    user = user_entry.get()
    password = password_entry.get()

    if(user, password) in accounts:
        login_window.pack_forget()
        mainPage.pack()
    else:
        message_label['text'] = "Falha, credenciais incorretas! Tente novamente!"

tk.Button(login_window, text="Login", command=verify_account).pack()

message_label = tk.Label(login_window)
message_label.pack()

mainPage = tk.Frame()
tk.Label(mainPage, text="Bem-Vindo ao MuTools!").pack()

loginWindow.mainloop()