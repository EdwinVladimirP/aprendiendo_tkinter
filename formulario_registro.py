import tkinter
from tkinter import *


def send_data():
    username_data = username.get()
    password_data = password.get()
    fullname_data = fullname.get()
    age_data = age.get()
    print(f"Usuario: ", username_data, "\t", "Password:", password_data, "\t", "Nombre completo: ", fullname_data, "\t",
          " Edad: ", age_data)
    newfile = open("registration.txt", "a")  # >se cambió de "w" a "a" (appen) para cololar nuevos datos al final.
    newfile.write(f"Usuario: " + username_data)
    newfile.write("\t")
    newfile.write(f"Password: " + password_data)
    newfile.write("\t")
    newfile.write(f"Nombre completo: " + fullname_data)
    newfile.write("\t")
    newfile.write(f"Edad: " + age_data)
    newfile.write("\n")
    newfile.close()
    # -------------->borrado de datos una ves enviados al archivo txt.
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)


ventana = Tk()
ventana.geometry("650x550")
ventana.title("Registro From | Python tkinter")
ventana.resizable(False, False)
ventana.config(background="#213141")
principal_title = Label(text="Registro From | Python tkinter | EdwinVladimirP", bg="#56CD63", font=("Cambria", 13),
                        fg="white", width="550", height="2")
principal_title.pack()

# ------------------>Campos del Formulario <----------------------

username_lbl = Label(text="Username:", bg="#FFEEDD")
username_lbl.place(x=22, y=70)

password_lbl = Label(text="Password:", bg="#FFEEDD")
password_lbl.place(x=22, y=130)

fullname_lbl = Label(text="Fullname:", bg="#FFEEDD")
fullname_lbl.place(x=22, y=190)

age_lbl = Label(text="Age:", bg="#FFEEDD")
age_lbl.place(x=22, y=250)

username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

# ------------------> Entrada de datos que se guardan en las variables de arriba

username_entry = Entry(textvariable=username, width=40)
password_entry = Entry(textvariable=password, width=40,
                       show="*")  # --> se usa show, par que no se vea lo que se escribe en ese campo.
fullname_entry = Entry(textvariable=fullname, width=40)
age_entry = Entry(textvariable=age, width=40)

# -----------------------> ubicando las entradas de datos

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
fullname_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)

# ---------------------->botón

submit_btn = Button(ventana, text="Submit info", command=send_data, width="30", height="2", bg="#00CD63")
submit_btn.place(x="22", y="320")

ventana.mainloop()
# https://www.youtube.com/watch?v=lLMFA7gMeY0
