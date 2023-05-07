from tkinter import *

root = Tk()


root.title("Label")

root.iconbitmap(".\luna.ico")
root.config(bg="MediumBlue")

miFrame = Frame(root, width=300, height=400)

miFrame.pack()
miFrame.config(bg="DodgerBlue")


minombre = StringVar()

# entradaInput = Entry(miFrame)
# entradaInput.place(x=50, y=25)
# entradaInput.config(bg="lightSkyBlue")

# nombreInput = Label(miFrame, text="nombre")
# nombreInput.place(x=50, y=25)


# para colocar los elementos es recomendable usar grid
entradaInput = Entry(miFrame, textvariable=minombre)
entradaInput.grid(row=0, column=1, pady=10)
entradaInput.config(bg="lightSkyBlue")

nombreInput = Label(miFrame, text="Nombre: ")
nombreInput.grid(row=0, column=0, sticky="e")
nombreInput.config(bg="DodgerBlue")

entradaInput1 = Entry(miFrame)
entradaInput1.grid(row=1, column=1, pady=10)
entradaInput1.config(bg="lightSkyBlue")

apellidoInput = Label(miFrame, text="Apellido: ")
apellidoInput.grid(row=1, column=0, sticky="e")
apellidoInput.config(bg="DodgerBlue")

entradaInput2 = Entry(miFrame)
entradaInput2.grid(row=2, column=1, pady=10)
entradaInput2.config(bg="lightSkyBlue")

direccionInput = Label(miFrame, text="Direccion de correo: ")
direccionInput.grid(row=2, column=0, sticky="e")
direccionInput.config(bg="DodgerBlue")
# creamos un campo de contraseña con show para que no nos la enseñe
entradaInput3 = Entry(miFrame)
entradaInput3.grid(row=3, column=1, pady=10)
entradaInput3.config(bg="lightSkyBlue", show="*")

passwordInput = Label(miFrame, text="Contraseña: ")
passwordInput.grid(row=3, column=0, sticky="e")
passwordInput.config(bg="DodgerBlue")


# Hay que añadir un tamaño porque por defecto es muy grande
# hay que crear una barra de scroll ya que no la crea
entradaInput4 = Text(miFrame, width=16, height=5)
entradaInput4.grid(row=4, column=1, pady=10)


comentarioInput = Label(miFrame, text="Comentarios: ")
comentarioInput.grid(row=4, column=0, sticky="e")
comentarioInput.config(bg="DodgerBlue")
# anadimos un sticky si lo deseamos en otra posicion
# sticky nos permite poner los textos alineados segun el punto cardinales
# para alinearlos a la derecha

# CREAMOS EL SCROLL le decimos command la variable dond queremos que aparezca y yview que sea vertical
scrollVert = Scrollbar(miFrame, command=entradaInput4.yview)
scrollVert.grid(row=4, column=2, sticky="nsew",  pady=10)
# creamos yscrollcommand para que se posicione en la barra donde estamos escribiendo
entradaInput4.config(bg="lightSkyBlue", yscrollcommand=scrollVert.set)


def codigoBoton():
    minombre.set("Pepito")


botonEnvio = Button(root, text="Enviar", command=codigoBoton)
botonEnvio.config(bg="DodgerBlue")
botonEnvio.pack()

root.mainloop()
