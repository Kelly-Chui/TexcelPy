import tkinter as tk

from Controller import TexcelController as Controller
from Model import TexcelModel as Model
from View import TexcelView as View

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Texcel")
        self.resizable(False, False)

        model = Model.TexcelModel()
        view = View.TexcelView(self)
        view.grid(padx=20, pady=20)

        controller = Controller.TexcelController(model, view)

if __name__ == '__main__':
    app = App()
    app.mainloop()
