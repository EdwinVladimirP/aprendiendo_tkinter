# https://www.youtube.com/watch?v=GFMxJa-RrRw
from tkinter import *


def mi_funcion():
    print("Jugamos al ahorcado?")


ventana = Tk()
ventana.geometry("400x200")
ventana.title("Hola Darkside")

lbl = Label(ventana, text="label creado por Darkside", fg='blue')
lbl.pack()

btn = Button(ventana, text="Press star to play",  command=mi_funcion)
btn.config( bg='blue', fg='yellow')  # ---------->método config------>configuración de sus propiedades
# btn[bg] = "blue" ------------->otra manera
# btn[fg] = "yellow"------------->otra manera
btn.pack()

ventana.mainloop()

"""from tkinter import Tk, Label, Button


def mensaje():
    print("Mensaje del botón")


ventana = Tk()  # ----->ventana creada apartir de una clase
ventana.geometry("400x280")
ventana.title("Darkside")

lbl = Label(ventana, text='Este es un [Label] tkinter')
lbl.pack()

btn = Button(ventana, text='Presiona este [Botton] para mensaje', command=mensaje)
btn.pack()

btn = Button(ventana, text='Otro botón!', command=mensaje)
btn.pack()
ventana.mainloop()"""
