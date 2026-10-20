#crear una ventanita que te diga que libro deberias leer
#usar un diccionario(valor y nombre del libro, posiblemente añadir un fanart)
#usar random
import os
import random
from time import sleep

#en proceso imaginativo
def biblioteca():
    libros={"Renegados": 1, "La mansion de la furias": 2, "Una corte de rosas y espinas": 3, "Asesino de brujas": 4,
        "Love you": 5, "Rojo, blanco y sangre azul": 6, "Una breve historia de casi todo": 7, "Fangirl": 8, "Carry on": 9, 
        "Un besi en Paris": 10, "El castillo ambulante": 11, "Fue un beso tonto":12, "El prince cruel":13, "Marfil" : 14, 
        "Los siete maridos de Evelyn Hugo": 15, "Al final mueren los dos": 16, "Caraval":17, "El val de la bruja": 18, 
        "Una educacion mortal":19, "Cinder":20, "El amor y otras maldiciones":21, "La hipotesis del amor":22, 
        "El reino de los malditos":23, "La caricia de la oscuridad":24, "El jardin de las mariposas":25, "Luna sin miel":26, 
        "Erase una vez un corazon roto":27, "Reino de las almas":28 , "Una obsesion perversa":29, "Ciudad medialuna":30, 
        "El vals de las hadas malditas":31, "De sangre y cenizas":32, "Hasta que nos quedemos con estrellas":33, 
        "Efectos colaterales del amor":34}
    return libros

def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def elegido():
    libros = biblioteca()
    while numero1==1:
        try:
            num=int(input("Ingrese un valor:"))
            if num in libros.values():
                print("Su libro es:",list(libros.keys())[list(libros.values()).index(num)])
                break
            else:
                print("Por favor ingrese un número válido entre 1 y 34.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entre 1 y 34.")
    if numero1==2:
            numero= random.randint(0,len(libros)-1)
            print("Su libro es:",list(libros.keys())[numero])
    
if __name__ =="__main__":
    limpiar()
    print("¿Desea elegir o prefiere que elijan por usted?")
    while True:
        try:
            numero1 = int(input("1. Usted elige\n2. Eligen por usted \n -> "))
            if numero1 in [1, 2]:
                break
            else:
                print("Por favor ingrese 1 o 2.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
    elegido()
    
