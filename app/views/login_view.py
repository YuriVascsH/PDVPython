import tkinter as tk

class LoginView:
    def __init__(self, root):
        self.root = root
        # Nome da Janela 
        self.root.title("Tela de Login")
        # Comando para chamar a o ícone:
        #self.root.Icombitmap("C:\Users\yuriv\Documents\PDVPython\images\logojocole.png")
        
        # Tamanho da janela 
        window_height = 400
        window_width = 600
                
        # Metodo para chamar o conteúdo da tela de login
        self.create_widgets()
        # Chamar o método para centralizar a janela
        self.center_screen(window_height, window_width)

    # Funcao para centralizar a tela no centro da tela:
    def center_screen(self, height, width):
        # Obter a largura e altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular a posição x e y para centralizar a janela
        pos_x = (screen_width // 2) - (width // 2)
        pos_y = (screen_height // 2) - (height // 2)

        # Definir a geometria da janela com a posição centralizada
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        #Defini que eu não consiga redimensionar a tela
        self.root.resizable(False, False)

    def create_widgets(self):
        self.icon_logo = tk.PhotoImage(file="images/logojocole.png")
        # Alterando a cor de fundo
        self.root.config(background='#446C65')
        label = tk.Label(self.root, image=self.icon_logo)
        label.pack()

root = tk.Tk()

# Inicializar a aplicação
app = LoginView(root)

# Iniciar o loop da janela
root.mainloop()
