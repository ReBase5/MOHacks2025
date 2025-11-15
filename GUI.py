# This file is for the Graphic User Interface

from tkinter import *

window = Tk()
window.geometry("800x800")
window.title("OceanGPT")
window.config(background = "#60b6d0")

titleLabel = Label(window, 
            text = "OceanGPT", 
            font = ('Currior', 50, 'bold'), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 12,
            padx = 20,
            pady = 20
            )       
titleLabel.pack()

askLabel = Label(window, 
            text = "Enter a time to get the tide at that time:", 
            font = ('Currior', 25,), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 8,
            padx = 10,
            pady = 10
            )       
askLabel.pack()

def click():
    print("The button was pressed; it would calculate the thing here.")

calcButton = Button(window,
                text = "Calculate",
                command = click,
                font = ("Currior", 20),
                fg = "#88FF88",
                bg = "#70c6e0",
                activeforeground = "#88FF88",
                activebackground = "#70c6e0",
                state = ACTIVE
                )
calcButton.pack()

window.mainloop()