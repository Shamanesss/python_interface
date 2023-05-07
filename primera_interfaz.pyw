from tkinter import *
# creamos la clase tk
raiz = Tk()


# dar titulo a la ventada
raiz.title("Nombre de la ventana")

# para redimensionar la ventana
# ancho width valor 0 booleano falso
# alto height valor 1 boleano true
raiz.resizable(1, 1)  # valor por defecto

# cambiar el icono
raiz.iconbitmap("luna.ico")

# cambiar el tamaño
raiz.geometry("650x350")
# para cambiar diferentes configuraciones usamos config
raiz.config(bg="LightSalmon")
# creamos y frame
miFrame = Frame()
# empaquetamos el frame


# usamos el metodo mainloop es necesario para que este en ejecucion
# siempre va a l final
raiz.mainloop()
