from tkinter import *
# creamos la clase tk
raiz = Tk()


# dar titulo a la ventada
raiz.title("Primer Frame")


# cambiar el icono
raiz.iconbitmap(".\luna.ico")
raiz.config(bg="LightSalmon")
# creamos y frame
miFrame = Frame()
# empaquetamos el frame dentro de su contenedor
miFrame.pack()
miFrame.config(bg="Tomato")
miFrame.config(width="650", height="350")

# para que se quede anclado en un lado
# miFrame.pack(side="left", anchor="nw")

# para que rellene la ventana cuando la hacemos grande se usa fill
# miFrame.pack(fill="x")

# para cambiar el borde y el ancho
miFrame.config(relief="groove")
miFrame.config(bd=35)

# cambiar el cursor a una clavera
miFrame.config(cursor="pirate")

# usamos el metodo mainloop es necesario para que este en ejecucion
# siempre va a l final
raiz.mainloop()
