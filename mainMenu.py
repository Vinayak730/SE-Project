import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog 
from tkinter.filedialog import asksaveasfile
from algorithms import *

window_width = 550
window_height = 400
file_contents = ''  # contains the contents of the file we choose

# This function is bound to the Browse Files button. The uploaded file's contents are stored in file_contents
def openFile():
    file = filedialog.askopenfilename(
        initialdir = 'C:/Users/ASUS/Documents',
        title = 'Select a File',
        filetypes=(('Text Files', '*.txt'),)
    )
    f = open(file, 'r')
    global file_contents
    file_contents = f.read()

def open_text_file(text): 
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())

def save_file(text):
    my_str1 = text  # read from one text box t1
    fob=filedialog.asksaveasfile(filetypes=[('text file','*.txt')],defaultextension='.txt',mode='w')
    try:
        fob.write(my_str1)
        fob.close()
    except :
        print (" There is an error...")

# This method is called from se.py and it creates the Encrypt/Decrypt window.  
def openWindow(master, screen_width, screen_height, title):
    newWindow = Toplevel(master)
    newWindow.title(title)
    global window_height, window_width
    
    xCoordinate = int(screen_width/2 - window_width/2)
    yCoordinate = int(screen_height/2 - window_height/2)
    newWindow.geometry('{}x{}+{}+{}'.format(window_width, window_height, xCoordinate, yCoordinate)) 
    if title == 'Encrypt': e_d_Window(newWindow, 0)
    elif title == 'Decrypt': e_d_Window(newWindow, 1)
    else: view_window(newWindow)

# this function basically deals with all the contents inside the encrypt/decrypt window.
def view_window(window):
    text = tk.Text(window, height=12,wrap = WORD, width = 67)
    text.grid(column=0, row=0, sticky='nsew')
    open_button = tk.Button(window,text='Open a File',command= lambda: open_text_file(text))
    open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

def e_d_Window(window, e_or_d):
    global window_height, window_width
    for i in range(11):
        window.rowconfigure(i, weight = 1)

    window.columnconfigure(0, weight = 1)
    window.columnconfigure(1, weight = 3)
    window.columnconfigure(2, weight = 3)
    window.columnconfigure(3, weight = 1)

    # option contains the value of the radiobutton
    option = IntVar()
    option1 = Radiobutton(window, text = 'Shift Cipher', variable = option, value = 0)

    '''
    this frame and text box is the one under the Caesar cipher radiobutton for taking Caesar cipher's key.
    Note: It's common practice to put text boxes inside their own frames to be able to size them properly.
    I've done the same for all text boxes in this program.
    '''
    scFrame = Frame(window, borderwidth = 1, relief = 'sunken', height = 50, width = 100)
    scKey = Text(scFrame)

    option1.grid(column = 1, row = 2, sticky = W)
    scFrame.grid(column = 1, row = 3, sticky = NW)
    scFrame.grid_propagate(False)
    scKey.grid()

    option2 = Radiobutton(window, text = 'Rail Fence Cipher', variable = option, value = 1)
    option2.grid(column = 1, row = 4, sticky = W)

    # frame and text box for input of rail fence cipher's key 
    rfcFrame = Frame(window, borderwidth = 1, relief = 'sunken', height = 50, width = 100)
    rfcKey = Text(rfcFrame)

    rfcFrame.grid(column = 1, row = 5, sticky = NW)
    rfcFrame.grid_propagate(False)
    rfcKey.grid()

    option3 = Radiobutton(window, text = 'Vignere Cipher', variable = option, value = 2)
    option3.grid(column = 1, row = 6, sticky = W)

    # frame and text box for input of vignere cipher's key 
    vcFrame = Frame(window, borderwidth = 1, relief = 'sunken', height = 50, width = 100)
    vcKey = Text(vcFrame)

    vcFrame.grid(column = 1, row = 7, sticky = NW)
    vcFrame.grid_propagate(False)
    vcKey.grid()
    
    '''
    frame and text box for the text box on the right side of the window where we display output of
    encryption/decryption algorithm
    '''
    container = Frame(window, borderwidth = 1, relief = 'sunken', height = window_height/1.1, width = window_width/1.5)
    container.grid(column = 2, row = 1, rowspan = 9, pady = 20)
    container.grid_propagate(False)
    rawText = Text(container, wrap = WORD, width = 45)
    rawText.grid()

    # Encrypt/Decrypt button at the bottom
    if not e_or_d:
        e_or_dButton = Button(window, text = 'Encrypt', command = lambda: selectAlgo(option.get(), [scKey.get('1.0',END), rfcKey.get('1.0',END), vcKey.get('1.0',END)], rawText, 0))
    else:
        e_or_dButton = Button(window, text = 'Decrypt', command = lambda: selectAlgo(option.get(), [scKey.get('1.0',END), rfcKey.get('1.0',END), vcKey.get('1.0',END)], rawText, 1))

    e_or_dButton.grid(column = 1, row = 8, sticky = W)

    save = Button(window, text = 'Save',command=lambda:save_file(rawText.get('1.0',END)))
    save.grid(column = 1,row = 9,sticky = W)

    # Browse files button
    chooseFile = Button(window, text = 'Browse Files', command = lambda: openFile())
    chooseFile.grid(column = 1, row = 1, sticky = W)

    window.mainloop()

''' 
this function is bound to the Encrypt/Decrypt button. We call the encryption/decryption algo in this
function and insert the result (plain text/cipher text) in the text box 
'''

def selectAlgo(opt, keys, textBox, e_or_d):
    global file_contents, scKey
    if not opt:
        if not e_or_d:
            sc = ShiftCipher(int(keys[0]))
            sc.plain_text = file_contents
            sc.encryption()
            textBox.insert(END, sc.cipher_text)
        else:
            sc = ShiftCipher(-1*int(keys[0]))
            sc.plain_text = file_contents
            sc.encryption()
            textBox.insert(END, sc.cipher_text)
    elif opt == 1:
        if not e_or_d:
            rfc = RailFence(int(keys[1]))
            rfc.plain_text = file_contents
            rfc.encryption()
            textBox.insert(END, rfc.cipher_text)
        else:
            rfc = RailFence(int(keys[1]))
            rfc.cipher_text = file_contents
            rfc.decryption()
            textBox.insert(END, rfc.plain_text)
    elif opt == 2:
        if not e_or_d:
            vc = VigenereCipher(keys[2])
            vc.plain_text = file_contents
            vc.encryption()
            textBox.insert(END, vc.cipher_text)
        else:
            vc = VignereCipher(keys[2])
            vc.cipher_text = file_contents
            vc.encryption()
            textBox.insert(END, vc.cipher_text)
