import tkinter as Tk

# def Hello():
#     label = Tk.Label(text="Hi learners, Welcomoe to tkinter tutorial", fg="white", bg="green")
#     label.pack()
ventana = Tk.Tk()
ventana.title("Aprendiendo tkinter")
ventana.geometry("600x500+300+150")

# ------------------------------->ejemplo 1
# label = Tk.Label(ventana, text="Hello learners, Welcome to tkinter Tutorial")
# label.place(x=190, y=210)

# label = Tk.Label(text="Hello learners, Welcome to tkinter Tutorial", fg="white", bg="#746AB0", width=50, height=10)
# label.place(x=190, y=210)
# ------------------------------->ejemplo
# boton = Tk.Button(text="Click me to say HI!", width=25, height=2, bg="white", fg="black", command=Hello)
# boton.pack()
# ------------------------------->ejemplo
# lbl = Tk.Label(text="name")
# entry = Tk.Entry()

# lbl.pack()
# entry.pack()

# ------------------------------->ejemplo
# name = Tk.Label(ventana, text="Name")
# name.place(x=30, y=50)
# email = Tk.Label(ventana, text="Email")
# email.place(x=30, y=90)
# password =Tk.Label(ventana, text="Password")
# password.place(x=30, y=130)


# e1 = Tk.Entry(ventana).place(x=100, y=50)
# e2 = Tk.Entry(ventana).place(x=100, y=90)
# e3 = Tk.Entry(ventana).place(x=100, y=130)
# ---------------------------------->fin ejemplo#

# ----------------------------------->ejemplo de frame
# frame_a = Tk.Frame()
# lbl_a = Tk.Label(master=frame_a, text= "This is frame A", bg="#4682B4")
# lbl_a.pack()

# frame_b = Tk.Frame()
# lbl_b = Tk.Label(master=frame_b, text="This is frame B", bg="#E9967A")
# lbl_b.pack()

# frame_a.pack()
# frame_b.pack()

# -------------------------------------->fin del ejemplo

border = {  # -----------------------Se creó un diccionario.
    "flat": Tk.FLAT,
    "sunken": Tk.SUNKEN,
    "raised": Tk.RAISED,
    "groove": Tk.GROOVE,
    "ridege": Tk.RIDGE
}
"""
import tkinter as Tk

# Crear un objeto Frame llamado "frame_a"
frame_a = Tk.Frame()

# Crear un objeto Label llamado "lbl_a" y colocarlo dentro de "frame_a"
lbl_a = Tk.Label(master=frame_a, text="This is frame A", bg="#4682B4")

# Colocar "lbl_a" dentro de "frame_a"
lbl_a.pack()

# Crear otro objeto Frame llamado "frame_b"
frame_b = Tk.Frame()

# Crear otro objeto Label llamado "lbl_b" y colocarlo dentro de "frame_b"
lbl_b = Tk.Label(master=frame_b, text="This is frame B", bg="#E9967A")

# Colocar "lbl_b" dentro de "frame_b"
lbl_b.pack()


# ----------------Explicación: 
# En este código, se crea el primer objeto Frame llamado frame_a utilizando la función Frame() sin pasar ningún argumento.
# Luego se crea un objeto Label llamado lbl_a y se especifica que el padre del objeto Label es frame_a utilizando el parámetro master. 
# El texto del Label es "This is frame A" y el color de fondo es "#4682B4". Luego, el Label se coloca dentro del Frame utilizando la función pack().

# A continuación, se crea otro objeto Frame llamado frame_b utilizando la misma función Frame() sin pasar ningún argumento. 
# Luego se crea otro objeto Label llamado lbl_b y se especifica que el padre del objeto Label es frame_b utilizando el parámetro master.
# El texto del Label es "This is frame B" y el color de fondo es "#E9967A". Luego, el Label se coloca dentro del Frame utilizando la función pack().

# Después de crear ambos Frame y sus Label correspondientes, se pueden colocar en la ventana principal utilizando la función pack().
# En este caso, no se especifica ningún argumento para la función pack(), por lo que los Frame se colocarán uno debajo del
# otro en el orden en que se llaman en el código. Al ejecutar este código, se mostrarán dos Frame con Label dentro de ellos en la ventana principal.
"""
ventana.mainloop()
# https://www.youtube.com/watch?v=PfZaJbZPYXs

"""
import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de pack()")

# Crear tres botones
boton1 = tk.Button(ventana, text="Botón 1")
boton2 = tk.Button(ventana, text="Botón 2")
boton3 = tk.Button(ventana, text="Botón 3")

# Organizar los botones usando pack()
boton1.pack()
boton2.pack()
boton3.pack()

# Iniciar el loop de la ventana
ventana.mainloop()
# https://www.youtube.com/watch?v=248temz_LD8
"""
