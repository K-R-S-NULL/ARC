'''
from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")
state_fullscreen = False
window.attributes("-fullscreen", state_fullscreen)

#window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")

def toggleFullscreen():
    global state_fullscreen
    state_fullscreen = not state_fullscreen
    window.attributes("-fullscreen", state_fullscreen)

btn_FScreenT = Button(window, text="_|", command=toggleFullscreen)
btn2 = Button(window, text="Click Me", command=clicked)

btn_FScreenT.grid(column=5, row=0)
btn2.grid(column=0, row=1)

window.mainloop()
'''


from tkinter import *
from tkinter import ttk

root = Tk()

#Tab Widget
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=TRUE)
tabs
frame1 = ttk.Frame(tabs)
frame2 = ttk.Frame(tabs)
tabs.add(frame1, text="Tab One",)
tabs.add(frame2, text="Tab Two")

root.geometry("400x240")
root.title("PythonLobby.com")
root.mainloop()