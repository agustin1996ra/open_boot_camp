"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la
cual debe de contener una lista de elementos seleccionables,
también debe de tener un label con el texto que queráis.
"""
import tkinter

window = tkinter.Tk()
window.title('Ejercicio 2 Tema 10')

texto = 'Seleccione su pais de nacimiento'
label_texto = tkinter.Label(window, text=texto, bg='black', fg='white')
label_texto.grid(column=0, row=0, padx=5, pady=5)

conoSur = ('Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador',
           'Peru', 'Paraguay', 'Uruguay', 'Venezuela')

paises = tkinter.Variable(value=conoSur)

lista_selecionable = tkinter.Listbox(window, listvariable=paises, height=4)
lista_selecionable.grid(column=0, row=1, padx=5, pady=5)


window.mainloop()
