import tkinter as tk

# Criando a janela principal
root = tk.Tk()
root.title("Formulário de Login")

# Configurando a largura mínima das colunas
root.grid_columnconfigure(0, minsize=100)  # Coluna 0
root.grid_columnconfigure(1, minsize=200)  # Coluna 1

# Criando e posicionando o label "Usuário"
usuario_label = tk.Label(root, text="Usuário:")
usuario_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # Alinhado à direita

# Criando e posicionando o campo de entrada de texto para o "Usuário"
usuario_entry = tk.Entry(root)
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

# Criando e posicionando o label "Senha"
senha_label = tk.Label(root, text="Senha:")
senha_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Criando e posicionando o campo de entrada de texto para a "Senha"
senha_entry = tk.Entry(root, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=10)

# Criando e posicionando o botão "Login"
login_button = tk.Button(root, text="Login")
login_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Iniciando o loop da aplicação
root.mainloop()
