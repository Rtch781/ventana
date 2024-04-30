import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("1024x960")



lnombre = tk.Label(ventana, text="Nombre:")
lnombre.grid(row = 0, column = 0)

entrynombre = tk.Entry(ventana)
entrynombre.grid(row = 0, column = 1)

lapellido = tk.Label(ventana, text="apellido:")
lapellido.grid(row = 1, column = 0)

entryapellido = tk.Entry(ventana)
entryapellido .grid(row = 1, column = 1)

sexo = tk.Label(ventana, text="sexo:")
sexo.grid(row = 2, column = 0)
rb_femenino = tk.Radiobutton(ventana, text="Femenino", variable=sexo, value="F", state="normal")
rb_femenino.grid(row=2, column=1)

rb_masculino = tk.Radiobutton(ventana, text="Masculino", variable=sexo, value="M", state="normal")
rb_masculino.grid(row=2, column=2)

lciudades= tk.Label(ventana, text="ciudad")
lciudades.grid(row=3, column=0)

ciudades = tk.Listbox(ventana)
ciudades.grid(row=3, column=1)

ciudades.insert(1, "Cartagena")
ciudades.insert(2, "Caracas")

button = tk.Button(ventana, text="Enviar")
button.grid(row=4, column=2)


ventana.mainloop()

