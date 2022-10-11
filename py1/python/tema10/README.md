# Interfaces gráficas de usuario (GUI)
- pygtk
- pyqt
- wxPython
- Tkinter

## Tkinter
Es una biblioteca que es un proyecto que se desprende TLC, este nós brinda una toolkit
para generar una interfaz gráfica, desde un script de python.

### Herramientas como:
Tkinter Designer, es una herramienta donde se le pueden da<r platillas de fliker.

### instalar tkinter  

## Geometría pack
La geometría pack se va a utilizar cuando queramos poner una cosa arriba de la otra, o 
una al lado de la otra.

```python
import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='Hola', bg='yellow', fg='blue')
label_saludo.pack(ipadx=50, ipady=50, fill='both')

label_adios = tkinter.Label(window, text='Adios', bg='red', fg='white')
label_adios.pack(ipadx=50, ipady=100, expand=True, fill='both')

window.mainloop()
```
```python
import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text='label1', bg='yellow', fg='blue')
label1.pack(ipadx=50, ipady=20, expand=True, fill='both')

label2 = tkinter.Label(window, text='label2', bg='purple', fg='white')
label2.pack(ipadx=50, ipady=20, expand=True, fill='both')

label3 = tkinter.Label(window, text='label3', bg='blue', fg='white')
label3.pack(ipadx=50, ipady=20, expand=True, fill='both')

label4 = tkinter.Label(window, text='label4', bg='red', fg='white')
label4.pack(ipadx=15, ipady=20, side='left', expand=True, fill='both')

label5 = tkinter.Label(window, text='label5', bg='yellow', fg='black')
label5.pack(ipadx=15, ipady=20, side='left', expand=True, fill='both')

label6 = tkinter.Label(window, text='label6', bg='green', fg='blue')
label6.pack(ipadx=20, ipady=20, side='left', expand=True, fill='both')

window.mainloop()
```

## Geometría grid
```python
import tkinter

# estructura de una geometría grid
# (0,0)  (1,0)  (2,0)
# (0,1)  (1,1)  (2,1)
# (0,2)  (1,2)  (2,2)
# (0,3)  (1,3)  (2,3)


window = tkinter.Tk()

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
login_button = tkinter.Button(window, text='Login')
login_button.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()
```
## Geometría Place

```python
import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text='Posicionamiento Absoluto', bg='blue', fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(window, text='Otro más', bg='red', fg='yellow')
label2.place(x=25, y=30)

window.mainloop()
```

```python
import random
import tkinter

window = tkinter.Tk()

colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black']

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = tkinter.Label(window, text=f'etiqueta {x}', bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))

window.mainloop()
```

## Componentes o widgets
- Frames o subventanas
- listbox (listas desplegables)
- 


