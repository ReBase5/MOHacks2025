# This file is for the Graphic User Interface

from tkinter import *
import threading
import time

window = Tk()
window.geometry("800x1000")
window.title("OceanGPT")
window.config(background = "#60b6d0")


def checkValues():
    if(len(timeEntry.get()) == 5 and timeEntry.get()[0:2].isdigit() and
    dayEntry.get().isdigit() and
    monthEntry.get().isdigit() and
    yearEntry.get().isdigit()
    ):
        if(int(dayEntry.get()) <= 31 and
        int(monthEntry.get()) <= 12 and
        int(yearEntry.get()) >= 2021
        ):
            calcButton.config(state = 'active')
        else:
            calcButton.config(state = 'disabled')
    else:
        calcButton.config(state = 'disabled')


def scheduleCheck():
    checkValues()
    timer = threading.Timer(0.04, scheduleCheck)
    timer.start()



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
titleLabel.place(x = 200, y = 10, width = 400)


# TIME \/ \/ \/
askTimeLabel = Label(window, 
            text = "Enter a time (HH:MM):", 
            font = ('Currior', 25,), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 8,
            padx = 10,
            pady = 10
            )       
askTimeLabel.place(x = 100, y = 160, width = 600)

timeEntry = Entry(window,
                 font = ("Arial", 25)
                 )
timeEntry.place(x = 100, y = 250, width = 400, height = 50)

def clickClearTime():
    timeEntry.delete(0, END)

clearTimeButton = Button(window,
                text = "Clear",
                command = clickClearTime,
                font = ("Currior", 20),
                fg = "#88FF88",
                bg = "#70c6e0",
                activeforeground = "#88FF88",
                activebackground = "#70c6e0",
                state = ACTIVE
                )
clearTimeButton.place(x = 550, y = 250, width = 150, height = 50)
# TIME /\ /\ /\


# DAY \/ \/ \/
askDayLabel = Label(window, 
            text = "Enter a day (DD):", 
            font = ('Currior', 25,), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 8,
            padx = 10,
            pady = 10
            )       
askDayLabel.place(x = 100, y = 310, width = 600)

dayEntry = Entry(window,
                 font = ("Arial", 25)
                 )
dayEntry.place(x = 100, y = 400, width = 400, height = 50)

def clickClearDay():
    dayEntry.delete(0, END)

clearDayButton = Button(window,
                text = "Clear",
                command = clickClearDay,
                font = ("Currior", 20),
                fg = "#88FF88",
                bg = "#70c6e0",
                activeforeground = "#88FF88",
                activebackground = "#70c6e0",
                state = ACTIVE
                )
clearDayButton.place(x = 550, y = 400, width = 150, height = 50)
# DAY /\ /\ /\


# MONTH \/ \/ \/
askMonthLabel = Label(window, 
            text = "Enter a month (MM):", 
            font = ('Currior', 25,), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 8,
            padx = 10,
            pady = 10
            )       
askMonthLabel.place(x = 100, y = 460, width = 600)

monthEntry = Entry(window,
                 font = ("Arial", 25)
                 )
monthEntry.place(x = 100, y = 550, width = 400, height = 50)

def clickClearMonth():
    monthEntry.delete(0, END)

clearMonthButton = Button(window,
                text = "Clear",
                command = clickClearMonth,
                font = ("Currior", 20),
                fg = "#88FF88",
                bg = "#70c6e0",
                activeforeground = "#88FF88",
                activebackground = "#70c6e0",
                state = ACTIVE
                )
clearMonthButton.place(x = 550, y = 550, width = 150, height = 50)
# MONTH /\ /\ /\

# YEAR \/ \/ \/
askYearLabel = Label(window, 
            text = "Enter a year (YY):", 
            font = ('Currior', 25,), 
            fg = '#88FF88', 
            bg = '#60b6d0',
            relief = RAISED,
            bd = 8,
            padx = 10,
            pady = 10
            )       
askYearLabel.place(x = 100, y = 610, width = 600)

yearEntry = Entry(window,
                 font = ("Arial", 25)
                 )
yearEntry.place(x = 100, y = 700, width = 400, height = 50)

def clickClearYear():
    yearEntry.delete(0, END)

clearYearButton = Button(window,
                text = "Clear",
                command = clickClearYear,
                font = ("Currior", 20),
                fg = "#88FF88",
                bg = "#70c6e0",
                activeforeground = "#88FF88",
                activebackground = "#70c6e0",
                state = ACTIVE
                )
clearYearButton.place(x = 550, y = 700, width = 150, height = 50)
# YEAR /\ /\ /\



def clickCalculate():
    time = timeEntry.get()
    day = int(dayEntry.get())
    month = int(monthEntry.get())
    year = int(yearEntry.get())
    print(f"The button was pressed; it would calculate the tide at {time} on {month}/{day}/{year}.")

calcButton = Button(window,
                text = "Calculate",
                command = clickCalculate,
                font = ("Currior", 20),
                fg = "#88FF88",
                bg = "#70c6e0",
                activeforeground = "#88FF88",
                activebackground = "#70c6e0",
                state = DISABLED
                )
calcButton.place(x = 325, y = 800, width = 150, height = 50)


scheduleCheck()


def displayTide():
        
    displayLabel = Label(window, 
                text = f"Tide level:\n{tidePrediction}", 
                font = ('Currior', 25,), 
                fg = '#88FF88', 
                bg = '#60b6d0',
                relief = RAISED,
                bd = 8,
                padx = 10,
                pady = 10
                )       
    displayLabel.place(x = 100, y = 950, width = 600)


window.mainloop()
