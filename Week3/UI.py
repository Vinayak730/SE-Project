
from tkinter import *
from tkinter import ttk
import tkinter as tk
#from Encryption_Algorithms import *
from User import *

def chooseFile():
    lblChooseFile = tk.Label(frame, text = "choose a file: ")
    lblChooseFile.grid(row=5,column=0)

    n = tk.StringVar()
    fileChosen = ttk.Combobox(frame, width = 27, textvariable = n)
  

# Adding combobox drop down list
    fileChosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    fileChosen.grid(column = 1, row = 5)
    fileChosen.current()
'''
class giveText():

    def __init__(self,frame):
        self.frame = frame
        self.lbl1 = tk.Label(self.frame, text = "enter you text here: ")
        self.lbl1.grid(row=2,column=0)

        self.inputtxt = tk.Text(self.frame,
                        height = 5,
                        width = 20)
        self.inputtxt.grid(row=2,column=1)
        self.lbl = tk.Label(self.frame, text = "")
        self.lbl.grid(row=4)

        #return self.inputtxt.get(1.0, "end-1c")
        
       

def printInput(input_box):
    inp = input_box.get(1.0, "end-1c")
    return inp
    self.lbl.config(text = "Provided Input: "+inp)

def clickButton(frame):
    # Button Creation
    printButton = tk.Button(frame,text = "Print",command=printInput(frame.inputtxt))
'''



def giveText():

    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "Provided Input: "+inp)
        #obj = module.user()
        user.text = inp


    lbl1 = tk.Label(frame, text = "enter you text here: ")
    lbl1.grid(row=2,column=0)

    inputtxt = tk.Text(frame,
                    height = 5,
                    width = 20)
    inputtxt.grid(row=2,column=1)

    # Function for getting Input
    # from textbox and printing it 
    # at label widge

    # Label Creation
    lbl = tk.Label(frame, text = "")
    lbl.grid(row=5)
    # Button Creation
    printButton = tk.Button(frame,
                            text = "Print", 
                            command = printInput)
    printButton.grid(row=4)
    
    #return printButton

def text_input():
    lblChoice = tk.Label(frame, text = "how do you want to encrypt: ").grid(row=0,column=0) 

    rb = IntVar()

    R1 = Radiobutton(frame, text = "give text", 
                    variable = rb, value = 1,command = lambda : giveText())
    R2 = Radiobutton(frame, text = "select a file", 
                    variable = rb, value = 2,command = lambda : chooseFile())
    R1.grid(row=0,column=1)
    R2.grid(row=1,column=1)

frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('500x400')

user = User()
#user.text = "xdwedfwedw"
text_input()
print(user.text)


frame.mainloop()


