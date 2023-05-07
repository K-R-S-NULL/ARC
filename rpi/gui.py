#
import tkinter as tk
class MainGUI:
    root = tk.Tk()
    def __init__(self) -> None:
        self.root = tk.Tk()
        message = tk.Label(self.root,text="TEXT")
        message.pack()
        pass
    def show(self) -> None:
        self.root.mainloop()
        pass
    def updateSpeed(self) -> None:
        pass
