# Importing all the necessary libraries
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from mainMenu import *

master = Tk()

# Tkinter codes to create and to center the window
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

window_width = 360
window_height = 360

xCoordinate = int(screen_width/2 - window_width/2)
yCoordinate = int(screen_height/2 - window_height/2)

master.title('The App')
master.geometry('{}x{}+{}+{}'.format(window_width, window_height, xCoordinate, yCoordinate))
label = tk.Label(master, text = "Classical encryption tutorial", bd = 25, fg = "black", font = "Castellar")
label.grid( column = 1, row = 0, sticky = 'nesw', pady = 10)
master.rowconfigure(0, weight = 7)

for i in range(1, 5):
    master.rowconfigure(i, weight = 1)

master.columnconfigure(0, weight = 1)
master.columnconfigure(1, weight = 1)  
master.columnconfigure(2, weight = 1)

'''
    Code to bind each of the button with its respective function. Here each button has its own corresponding actions.
    The buttons include ENCRYPT, DECRYPT, VIEW and EXIT
    ENCRYPT - Opens a window where the user can encrypt the contents present in a text file
    DECRYPT - Opens a window where the user can decrypt the contents present in a text file
    VIEW - Opens a window where the user can see all the contents present in a particular text file.
    EXIT - Closes all the programs

    All the operations of each of the function is defined and gets redirected to the mainmenu.py file
'''
e  = Button(master, text = 'ENCRYPT', command = lambda: openWindow(master, screen_width, screen_height, 'Encrypt'),)
d  = Button(master, text = 'DECRYPT', command = lambda: openWindow(master, screen_width, screen_height, 'Decrypt'))
v  = Button(master, text = 'VIEW', command = lambda: openWindow(master, screen_width, screen_height, 'view'))
ex = Button(master, text = "EXIT",command = master.destroy)

# Additional codes for padding the buttons

e.grid( column = 1, row = 1, sticky = 'nesw', pady = 10)
d.grid( column = 1, row = 2, sticky = 'nesw', pady = 10)
v.grid( column = 1, row = 3, sticky = 'nesw', pady = 10)
ex.grid(column = 1, row = 4, sticky = 'nesw', pady = 10)

master.mainloop()
