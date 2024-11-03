import tkinter as tk
from random import randint, choice
from tkinter import messagebox

def AddIdea():
    value = EnterText.get()
    if value != '':
        with open('How.txt', 'a+', encoding='utf-8') as file:
            file.write(value + '\n')
        # Очищаем поле ввода EnterText, удаляя весь текст от начальной до конечной позиции.
        EnterText.delete(0, 'end')
    else:
        tk.messagebox.showinfo('Error', ('Entering area is empty.'))

def RandomIdea():
    with open('How.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        tk.messagebox.showinfo('Idea', (choice(lines)))

def EnterClick(e):
    AddIdea()

window = tk.Tk()

window.resizable(width=False, height=False)

window.title('Idea generator')

window.geometry('720x360')

window['bg'] = 'black'

idea = tk.Label(window, text='Add an idea', font=('Arial Bold', 14), fg='white', bg='black')
idea.place(x=290, y=25)

EnterText = tk.Entry(fg='black', width=47)
EnterText.place(x=220, y=65)

btn = tk.Button(window, text='Add', command=AddIdea, width='40', height='2', fg='black', bg='white')
btn.place(x=220, y=110)

window.bind('<Return>', EnterClick)

GiveIdea = tk.Label(window, text='Generate an idea', font=('Arial Bold', 14), fg='white', bg='black')
GiveIdea.place(x=270, y=175)

btn = tk.Button(window, text='Show idea', command=RandomIdea, width='40', height='2', fg='black', bg='white')
btn.place(x=220, y=210)


window.mainloop()

