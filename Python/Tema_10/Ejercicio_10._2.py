# En este segundo ejercicio, tendréis que crear una interfaz sencilla 
# la cual debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.

import tkinter as tk

vent = tk.Tk()
vent.title('TEMA 10 - Ejercicio 2')
vent.geometry('300x250')

paises = ['Colombia', 
    'Peru', 
    'Chile',
    'Costa Rica',
    'Venezuela',
    'Argentina',
    'Mexico',
    'Brazil',
    'Nicaragua',
    'Ecuador'
    ]

# lista
lista1 = tk.Listbox(vent, justify='center', selectbackground='green')
for item in paises:
    lista1.insert(tk.END, item)
lista1.pack(pady=10)

# Label 1
l1 = tk.Label(vent, text='Listado de paises')
l1.pack()

vent.mainloop()