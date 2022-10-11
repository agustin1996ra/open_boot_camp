import tkinter

# estructura de una geometría grid
# (0,0)  (1,0)  (2,0)
# (0,1)  (1,1)  (2,1)
# (0,2)  (1,2)  (2,2)
# (0,3)  (1,3)  (2,3)


window = tkinter.Tk()

window.geometry("800x600")

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=3)


# Usuario
# Etiqueta usuario
username_label = tkinter.Label(window, text='Username:')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# Campo usuario
username_entry = tkinter.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# Password
# Etiqueta password
password_label = tkinter.Label(window, text='Password')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# Campo password
password_entry = tkinter.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)


# Boton
def click(event):
    print('Han hecho click en loging')


login_button = tkinter.Button(window, text='Login')
login_button.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)
login_button.bind('<Button-1>', click)  # Esto es un evento


# Botón salir
def salir(event):
    print('Adios')
    window.quit()


exit_button = tkinter.Button(window, text='Salir')
exit_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)
exit_button.bind('<Button-1>', salir)  # Esto es un evento

window.mainloop()
