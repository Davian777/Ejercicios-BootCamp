# En este ejercicio tenéis que crear una lista de RadioButton 
# que muestre la opción que se ha seleccionado y que contenga 
# un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

import tkinter as tk

vent = tk.Tk()
vent.title('TEMA 10 - Ejercicio 1')
vent.geometry('300x200')

var = tk.StringVar()

def mostrar():
    l1.config(text=var.get())

def reset():
    l1.config(text='')

# Radiobutton 1
r1 = tk.Radiobutton(vent, text='Python', variable=var, value='Python',command=mostrar)
r1.grid(column=0, row=0, padx=5)

# Radiobutton 2
r2 = tk.Radiobutton(vent, text='Java', variable=var, value='Java',command=mostrar)
r2.grid(column=1, row=0, padx=5)

# Radiobutton 3
r3 = tk.Radiobutton(vent, text='C ++', variable=var, value='C ++',command=mostrar)
r3.grid(column=2, row=0, padx=5)

# Radiobutton 4
r4 = tk.Radiobutton(vent, text='Rust', variable=var, value='Rust',command=mostrar)
r4.grid(column=3, row=0, padx=5)

# Label 1
l1 = tk.Label(vent, text="")
l1.grid(columnspan=4, pady=40)
l1.config(fg='red', font=('helvetica','24'))

# btn1
b1 = tk.Button(vent, text='Reiniciar', command=reset)
b1.grid(columnspan=4, pady=5)

vent.mainloop()