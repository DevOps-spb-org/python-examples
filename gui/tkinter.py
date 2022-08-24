from tkinter import *

root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")

clicks = 0


def click_button():
    global clicks
    clicks += 1
    root.title("Кликов {}".format(clicks))


btn = Button(text="Привет",  # текст кнопки
             background="#555",  # фоновый цвет кнопки
             foreground="#ccc",  # цвет текста
             padx="20",  # отступ от границ до содержимого по горизонтали
             pady="8",  # отступ от границ до содержимого по вертикали
             font="16",  # высота шрифта
             command=click_button
             )
btn.pack()

root.mainloop
