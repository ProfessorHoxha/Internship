#https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/
#Demystifying Cybercrime, The Risk management Group
#https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Form_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        options = {'padx': 0, 'pady': 200}

        label_one = ttk.Label(self, text='Form')
        label_one.pack(**options)   

        self.pack(**options)
         
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('TRMG')
        self.geometry('800x500')
    def Label(self):
        #Demystifying Cybercrime
        label_one = tk.Label(self, text="Demystifying Cybercrime", font=("Arial", 25))
        label_one.place(x=200, y=0)
        
        #The Risk management Group
        label_two = tk.Label(self, text="The Risk management Group", font=("Arial", 20))
        label_two.place(x=200, y=40)

    def image(self):
        pass

#mainloop
if __name__ == "__main__":
    app = App()
    # configure the root window
    app.title('TRMG')
    app.geometry('1000x800')
    form = Form_frame(app)

    app.Label()
    app.mainloop()
