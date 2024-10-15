from tkinter import *

class LoginView:
    def __init__(self, root):
        self.root = root
        # Nome da Janela 
        self.root.title("Tela de Login")
        
        # Tamanho da janela 
        window_height = 300
        window_width = 350
        
        # Chamar o método para centralizar a janela
        self.center_screen(window_height, window_width)
        
        # Método para chamar o conteúdo da tela de login
        self.create_widgets()

    # Função para centralizar a tela no centro da tela
    def center_screen(self, height, width):
        # Obter a largura e altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular a posição x e y para centralizar a janela
        pos_x = (screen_width // 2) - (width // 2)
        pos_y = (screen_height // 2) - (height // 2)

        # Definir a geometria da janela com a posição centralizada
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        # Definir que a janela não possa ser redimensionada
        self.root.resizable(False, False)

    def create_widgets(self):
        # Carregar a imagem do logo (certifique-se de que o caminho esteja correto)
        self.icon_logo = PhotoImage(file="images/logojocole.png")
        
        # Alterando a cor de fundo
        self.root.config(background='#446C65')
        
        # Icone (Logo)
        self.label_logo = Label(self.root, image=self.icon_logo, bg='#446C65')
        self.label_logo.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

        # Label e input Usuário
        self.usuario_label = Label(self.root, text="Usuário", bg='#446C65', fg='white', font=("Arial", 12), padx=30)
        self.usuario_label.grid(row=1, column=0,sticky="w")

        self.usuario_entry = Entry(self.root, width=30)
        self.usuario_entry.grid(row=1, column=1, sticky="w", columnspan=2)

        # Label e input Senha
        self.usuario_label = Label(self.root, text="Senha", bg='#446C65', fg='white', font=("Arial", 12), padx=30, pady=20)
        self.usuario_label.grid(row=2, column=0,sticky="w")

        self.usuario_entry = Entry(self.root, width=30, show="*")
        self.usuario_entry.grid(row=2, column=1, sticky="w", columnspan=2)

        # Butão logar
        self.btn_logar = Button(self.root, text="Logar", bg="green", fg="white", padx=10, pady=10, command=realizar_login)
        self.btn_logar.grid(row=3,column=2) 

        # Ajustar as colunas para ocupar o espaço disponível
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

root = Tk()

# Inicializar a aplicação
app = LoginView(root)

# Iniciar o loop da janela
root.mainloop()
