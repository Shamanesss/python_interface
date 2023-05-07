from tkinter import *

root = Tk()

root.title("Label")

root.iconbitmap(".\luna.ico")
root.config(bg="SeaGreen")

miFrame = Frame(root, width=700, height=400)

miFrame.pack()
miFrame.config(bg="PaleGreen")

# introducimos un label

milabel = Label(miFrame, text="Este es el primer label",
                fg="white", font=(18), bg="PaleGreen")
milabel.place(x=200, y=20)
# el codigo se puede abreviar si no lo var a reutilizar de esta manera
# Label(miFrame, text="Este es el primer label").place(x=100, y=200)

# para poner una imagen
miImage = PhotoImage(file=".\\label\\mar.gif")
Label(miFrame, image=miImage).place(x=25, y=75)

root.mainloop()
