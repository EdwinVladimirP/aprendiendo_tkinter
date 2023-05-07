"""Posicionar controles dentro de una ventana
gestores de geometría
-definir el modo en que deben colocarse los widgets(controles) dentro de una ventana
*place
*pack
*grid
-para construir las ventanas se pueden utilizar unos widgets especiales(marcos, paneles, etc)
que actúan como contenedores de otros widgets. Estos widgets se utilizan para agrupar
varios controles.
-NO DEBEN MEZCLARSE DISTINTOS MÉTODOS dentro de un mismo contenedor.
 https://www.youtube.com/watch?v=y69rqjEfwYI

Posición absoluta
Place
*permite ubicar elementos indicando su posición (X e Y) respecto de un elemento padre.
self.button.place(x=60, y=40, width=100, height=30)

ojo: Comienza desde la parte superior izquierda hacia la parte inferior derecha. se habla de pixeles.

*Valores ABSOLUTOS
 """

"""Posición Relativa: 
Place: 
*permite ubicar elementos indicando su posición (X e Y) respecto de un elemento padre.


button.place(relx=0.1, rely=0.1, relwidth= 0.5, relheight=0.5)
                                    |                   |                   |                               |
                                    |                   |                   |                               |
        La ubicación en estos casos de relx, rely, relwidth, relheight
        hace referencia al porcentaje de la pantalla; ejemplo: 
        0.1 es igual al 10% de la pantalla en el eje x
        0.1 es igual al 10% de la pantalla en el eje y
        0.5 es igual al 50% de la pantalla en ancho 
        0.5 es igual al 50% de la pantalla en alto
        ACEPTAN VALORES ENTRE 0 Y 1. 
"""

"""hola prueba"""

from tkinter import Tk, Label, Button, Entry

ventana = Tk()
ventana.title("ejemplo de place")
ventana.geometry("400x200")


def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)


# Cuando se usa valores relativos, los elementos se acomodan(crecen, cambian de tamaño) en relación al porcentaje.
# lo que NO sucede si se usan las propiedades absolutas.

lbl1 = Label(ventana, text="Primer número", bg="yellow")
lbl1.place(relx=0.03, rely=0.04, relwidth=0.23, relheight=0.1)
txt1 = Entry(ventana, bg="pink")
txt1.place(relx=0.3, rely=0.04, relwidth=0.22, relheight=0.1)

btn1 = Button(ventana, text="Sumar", command=fnSuma)
btn1.place(relx=0.55, rely=0.17, relwidth=0.20, relheight=0.1)

lbl2 = Label(ventana, text="Segundo número", bg="yellow")
lbl2.place(relx=0.03, rely=0.17, relwidth=0.23, relheight=0.1)
txt2 = Entry(ventana, bg="pink")
txt2.place(relx=0.3, rely=0.17, relwidth=0.22, relheight=0.1)

lbl3 = Label(ventana, text="Resultado", bg="yellow")
lbl3.place(relx=0.03, rely=0.35, relwidth=0.23, relheight=0.1)
txt3 = Entry(ventana, bg="pink")
txt3.place(relx=0.3, rely=0.35, relwidth=0.22, relheight=0.1)

ventana.mainloop()
"""
Con Valores Absolutos: 

from tkinter import Tk, Label, Button, Entry

ventana = Tk()
ventana.title("ejemplo de place")
ventana.geometry("400x200")


def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)
    



lbl1 = Label(ventana, text="Primer número", bg="yellow")
lbl1.place(x=10, y=10, width=100, height=30)
txt1 = Entry(ventana, bg="pink")
txt1.place(x=120, y=10, width=100, height=30)
btn1 = Button(ventana, text="Sumar", command=fnSuma)
btn1.place(x=230, y=80)

lbl2 = Label(ventana, text="Segundo número", bg="yellow")
lbl2.place(x=10, y=50, width=100, height=30)
txt2 = Entry(ventana, bg="pink")
txt2.place(x=120, y=50, width=100, height=30)

lbl3 = Label(ventana, text="Resultado", bg="yellow")
lbl3.place(x=10, y=120, width=100, height=30)
txt3 = Entry(ventana, bg="pink")
txt3.place(x=120, y=120, width=100, height=30)

ventana.mainloop()"""
