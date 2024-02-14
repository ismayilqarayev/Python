import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('IQ')
        self.geometry('500x300')

        self.label = ttk.Label(self, text='uran')
        self.button_1 = ttk.Button(self, text='run')
        self.button_2 = ttk.Button(self, text='stop')
        self.button_3 = ttk.Button(self, text='start')

        self.button_1['command'] = self.button_clicked_1
        self.button_2['command'] = self.button_clicked_2
        self.button_2['command'] = self.button_clicked_3

        self.label.pack()
        self.button_1.pack()
        self.button_2.pack()
        self.button_3.pack()

    def button_clicked_1(self):
        showinfo(title='info', message='-------')

    def button_clicked_2(self):
        showinfo(title='info', message='#####')

    def button_clicked_3(self):
        showinfo(title='info', message='#####')


if __name__ == "__main__":
    app = App()
    app.mainloop()


