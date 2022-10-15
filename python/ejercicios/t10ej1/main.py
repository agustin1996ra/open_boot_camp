"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se
ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""
import tkinter

window = tkinter.Tk()

label_titulo = tkinter.Label(window, text='Ejercicio 1 tema 10', bg='black', fg='white')
label_titulo.grid(column=0, row=0, pady=5, padx=5)

seleccionado = tkinter.StringVar()


# Función de reinicio de los Radiobutton
def reset_rb(event):
    seleccionado.set('')


# RadioButton
rb_si = tkinter.Radiobutton(window, text='Si', value='1', variable=seleccionado)
rb_no = tkinter.Radiobutton(window, text='No', value='2', variable=seleccionado)
rb_nose = tkinter.Radiobutton(window, text='No sabe/No contesta', value='3', variable=seleccionado)

# Posicionamiento
rb_si.grid(column=0, row=2, pady=5, padx=5, sticky=tkinter.W)
rb_no.grid(column=0, row=3, pady=5, padx=5, sticky=tkinter.W)
rb_nose.grid(column=0, row=4, pady=5, padx=5, sticky=tkinter.W)

# Botón de reinicio
reset_boton = tkinter.Button(window, text='Reiniciar respuesta')
reset_boton.grid(column=0, row=5, pady=5, padx=5)
reset_boton.bind('<Button-1>', reset_rb)

window.mainloop()
