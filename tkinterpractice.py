#https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/
#import library
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        #label
        self.label = ttk.Label(self, text="Testing 123")
        self.label.pack(**options)
        
        #button
        self.button = ttk.Button(self, text='Click Me', command=self.button_clicked)  
        self.button.pack(**options)

        #show the frame on the container
        self.pack(**options)

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('My Awesome App')
        self.geometry('700x500')

#mainloop
if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
