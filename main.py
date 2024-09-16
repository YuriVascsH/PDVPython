from tkinter import Tk
from app.views.login_view import LoginView

if __name__ == "__main__":
    root = Tk()
    app = LoginView(root)
    root.mainloop()
