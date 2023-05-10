"""
En este código se crea un diccionario llamado border con cinco elementos.
Cada elemento es una cadena de texto que representa un estilo de borde diferente y su valor es
una constante definida en el módulo Tk de la biblioteca tkinter.

Las constantes en el módulo Tk se utilizan para especificar el estilo del borde de un widget.
Los cinco estilos de borde disponibles son:

Tk.FLAT: El widget no tiene borde.
Tk.SUNKEN: El widget se hunde en el marco principal.
Tk.RAISED: El widget se eleva sobre el marco principal.
Tk.GROOVE: El widget tiene un borde en relieve con un patrón de ranura.
Tk.RIDGE: El widget tiene un borde en relieve con un patrón de cresta.
El diccionario border asigna una cadena de texto a cada una de estas constantes, lo que hace que sea más fácil
para el programador especificar el estilo de borde deseado al crear un widget.

Por ejemplo, si se quisiera crear un botón con un borde hundido, se podría utilizar el siguiente código:
"""

import tkinter as Tk

border = {
    "flat": Tk.FLAT,
    "sunken": Tk.SUNKEN,
    "raised": Tk.RAISED,
    "groove": Tk.GROOVE,
    "ridge": Tk.RIDGE
}

ventana = Tk.Tk()
ventana.geometry("500x500")

boton = Tk.Button(ventana, text="Presioname", borderwidth=5, relief=border["sunken"])
boton.pack()

ventana.mainloop()

"""
En este código, se crea un objeto Button llamado boton y se le asigna el estilo de borde Tk.SUNKEN
utilizando la constante correspondiente en el diccionario border.
El parámetro borderwidth se utiliza para especificar el ancho del borde en píxeles.
El botón se coloca en la ventana principal utilizando la función pack(). Al ejecutar este código,
se mostrará un botón con un borde hundido en la ventana principal.
"""