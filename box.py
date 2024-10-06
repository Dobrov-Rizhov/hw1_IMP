from tkinter import Tk, Button, Label
import customtkinter
from application.salary import *

def box():
    def click_me():
        labbel2['text'] = 'получишь результат :)'
    root = customtkinter.CTk()
    root.title('Бухгалтерия')
    root.geometry('250x80')
    labbel1 = customtkinter.CTkLabel(root, text='Нажми на кнопку')
    labbel1.pack()
    labbel2 = Label(root, text='?????')
    labbel2.pack()
    button = customtkinter.CTkButton(root, text='Нажми меня', command=click_me)
    button.pack()

    root.mainloop()








