#crear una ventanita que te diga datos de tu signo

import os
from tkinter import Entry, Label, ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox


def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

#la funcion caja corresponde a la palabra que recibe la cajatexto
def caja():
    texto=cajatexto.get().lower()
    print(texto)
    if texto == "aries":
        print(messagebox.showinfo(message="fecha: 21/03 hasta 19/04 \nelemento: fuego \ncolor: rojo \nplaneta: marte \nsigno puesto: libra \nRasgos: \n->Trabajadores \n->Falta de paciencia \n->Rencorosos"))
    elif texto == "tauro":
        print(messagebox.showinfo(message="fecha: 20/04 hasta 20/05 \nelemento: tierra \ncolor: verde y azul \nplaneta: venus \nsigno opuesto: escorpio \nRasgos: \n->Tranquilos \n->Mucha paciencia \n->Gruñones y rencorosos"))
    elif texto == "geminis":
        print(messagebox.showinfo(message="fecha: 21/05 hasta 20/06 \nelemento: aire \ncolor: amarillo \nplaneta: mercurio \nsigno opuesto: sagitario \nRasgos: \n->divertidos y amables \n->mentirosos y superficiales"))
    elif texto =="cancer":
        print(messagebox.showinfo(message="fecha: 21/06 hasta 22/07 \nelemento: agua \ncolor: Blanco, Gris y Violeta \nplaneta: Luna \nsigno opuesto: capricornio \nRasgos: \n-> amables y elocuentes \n->irritantes y rencorosos"))
    elif texto =="leo":
        print(messagebox.showinfo(message="fecha: 23/07 hasta 22/04 \nelemento: fuego \ncolor: amarillo \nplaneta: sol \nsigno opuesto: acuario \nRasgos: \n->generoso y lideres \n-> prepotentes e inmaduros"))
    elif texto == "virgo":
        print(messagebox.showinfo(message="fecha: 23/08 hasta 22/09 \nelemento: tierra \ncolor: verde oscuro \nplaneta: mercurio \nsigno opuesto: piscis \nRasgos: \n->Analitico y paciente \n->Persistente y controlador"))
    elif texto =="libra":
        print(messagebox.showinfo(message="fecha: 23/09 hasta 22/10 \nelemento: aire \ncolor: dorado \nplaneta: venus \nsigno opuesto: aries \nRasgos: \n->sociales y delicados \n->indecisos y superficiales"))
    elif texto == "escorpio":
        print(messagebox.showinfo(message="fecha: 23/10 hasta 21/11 \nelemento: agua  \ncolor: granate \nplaneta: plutón \nsigno opuesto: tauro \nRasgos: \n->razonadores y consejeros \n->desconfiados y envidiosos"))
    elif texto == "sagitario":
        print(messagebox.showinfo(message="fecha: 22/11 hasta 21/12 \nelemento: fuego \ncolor: purpura, azul y violeta \nplaneta: júpiter \nsigno opuesto:gemenis \nRasgos: \n-> alegres y estudiosos \n-> radicales y caprichosos"))
    elif texto == "capricornio":
        print(messagebox.showinfo(message="fecha: 22/12 hasta 20/01 \nelemento: tierra \ncolor: marrón y negro \nplaneta: saturno \nsigno opuesto: cáncer \nRasgos: \n->ambiciosos y cuidadosos \n-> pesimistas y rencorosos"))
    elif texto == "acuario":
        print(messagebox.showinfo(message="fecha: 21/01 hasta 19/02 \nelemento: aire \ncolor: turquesa \nplaneta: urano \nsigno opuesto: leo \nRasgos: \n-> altruistas \n-> imprevisibles"))
    elif texto == "piscis":
        print(messagebox.showinfo(message="fecha: 20/02 hasta 20/03 \nelemento: agua \ncolor: verde \nplaneta: neptuno \nsigno opuesto: virgo \nRasgos: \n->romanticos y cariñosos \n-> despistados"))
    elif texto == "sofi" or texto == "sofia":
        print(messagebox.showinfo(message= "la hermosa creadora"))
    else:
        print(messagebox.showinfo(message="no corresponde a un signo zodiacal"))


def cerrar():
    messagebox.askyesno(message='Seguro de que quieres salir?',icon='question' ,title='Salir')
    raiz.destroy()


#esta es la ventana 
raiz = tk.Tk() 
raiz.title("Signos") #nombre de la ventana
raiz.geometry("320x300") #tamaño


#es el texto del inicio 
etiqueta= tk.Label(raiz, text="Ingresa tu signo: ")
etiqueta.pack()
  
#entrada de información
cajatexto = tk.Entry(justify=tk.CENTER)
cajatexto.pack()

boton= ttk.Button(raiz, text="click", command=caja)
boton.pack()

#imagen   
imagen = ImageTk.PhotoImage(file="tkpng.png")
label= Label(image=imagen)
label.pack()

#boton para cerrar
boton2= ttk.Button(raiz, text="cerrar",command=cerrar)
boton2.pack()

raiz.mainloop() #comando importante para se que ejecute la ventanita


if __name__ == "__main__":
    limpiar() #está de lindo porque no funciona:)
    messagebox.showinfo(message=caja())



