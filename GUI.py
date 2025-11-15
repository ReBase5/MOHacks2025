# This file is for the Graphic User Interface

from tkinter import *

window = Tk()
window.geometry("512x512")
window.title("OceanGPT")
window.config(background = "#60b6d0")

label = Label(window, 
            text = "OceanGPT\nEnter a time to get the tide at that time:", 
            font = ('Currior', 40, 'bold'), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 10,
            padx = 20,
            pady = 20
            )       
label.pack()

def click():
    

button = Button(window,
                text = "Calculate",
                command = click
                )
button.pack()

window.mainloop()