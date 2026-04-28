import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

ventprincipal = tk.Tk() #Crea la ventana principal
ventprincipal.title('Proyecto StrangerTEC') #El título de la ventana
ventprincipal.geometry("750x750") #Ajusta el tamaño de la ventana
ventprincipal.resizable(width=False, height=False) #Hace que el usuario no pueda cambiar las dimensiones de la ventana

canvaprincipal = tk.Canvas(ventprincipal, width= 742, height= 742, bg= "black") #Crea el canva (donde se coloca el tecto, botones, etc)

imagen = Image.open("Background.png")  # cambia por el nombre de tu archivo
imagen = imagen.resize((742, 742))  # ajusta al tamaño de la ventana
fondo = ImageTk.PhotoImage(imagen)

# Poner imagen en el canvas
canvaprincipal.create_image(0, 0, image=fondo, anchor="nw")

canvaprincipal.create_text(371, 310, text= 'Stranger', fill= '#D7271E' , font= ('Stranger Things Outlined', 70)) #Crea el texto que aparece en la ventana
canvaprincipal.create_text(371, 380, text= 'TEC', fill= '#D7271E' , font= ('Stranger Things Outlined', 67))
canvaprincipal.create_text(65, 22, text= 'Jocsan Calvo', fill= 'white' , font= ('Benguiat Bold', 10))
canvaprincipal.create_text(672, 22, text= 'Fabricio Guillén', fill= 'white' , font= ('Benguiat Bold', 10))
text = canvaprincipal.create_text(371, 500, text= '', fill = 'white' , font= ('Benguiat Bold', 12)) #Variable para que el texto pueda parpadear


estado = {'Parpadear': True} #Variable para controlar el estado del parpadeo

#Función para que el texto indicado parpadee cada cierto tiempo
def parpadear():
    if not estado["Parpadear"]:
        return
    mtexto = canvaprincipal.itemcget(text, 'text') #Obtiene el texto que contiene la variable text
    
    if mtexto == '':
        canvaprincipal.itemconfig(text, text= 'Presione cualquier tecla para continuar') #Si no hay texto, escribe el mensaje indicado

    else:
        canvaprincipal.itemconfig(text, text= '') #Si ya hay texto, borra el mensaje indicado
    
    ventprincipal.after(750, parpadear) #Hace que la función se ejecute cada 750 milisegundos


def continuar(event = None):
    estado["Parpadear"] = False
    ventprincipal.unbind("<Key>") #Deja de ejecutar la función 'continuar' al tocar cualquier tecla
    menu()
   
def menu():
    canvaprincipal.delete("all") #Borra todo lo que hay en el canva
    canvaprincipal.create_text(371, 110, text= 'Bienvenido', fill= '#D7271E' , font= ('Stranger Things Outlined', 65)) #Crea el texto que aparece en la ventana
    canvaprincipal.create_text(371, 250, text= 'Escriba los nombres de los jugadores:', fill= 'white' , font= ('Benguiat Bold', 10))

    global username1, username2, botoncontinuar

    canvaprincipal.create_text(371, 310, text= 'Jugador 1', fill= 'white' , font= ('Benguiat Bold', 12)) #Crea el texto que indica el campo de texto para el jugador 1
    username1 = tk.Entry(canvaprincipal, font= ('Benguiat Bold', 12), fg= 'white', background= 'black', insertbackground= 'white', highlightbackground= '#D7271E', highlightthickness = 2, relief= 'solid', justify= 'center') #Crea un campo de texto para que el usuario escriba su nombre de usuario
    username1.place(x= 371, y= 350, anchor="center") #Posiciona el campo de texto en el canva

    canvaprincipal.create_text(371, 390, text= 'Jugador 2', fill= 'white' , font= ('Benguiat Bold', 12)) #Crea el texto que indica el campo de texto para el jugador 2
    username2 = tk.Entry(canvaprincipal, font= ('Benguiat Bold', 12), fg= 'white', background= 'black', insertbackground= 'white', highlightbackground= '#D7271E', highlightthickness = 2, relief= 'solid', justify= 'center') #Crea un campo de texto para que el usuario escriba su nombre de usuario
    username2.place(x= 371, y= 430, anchor="center") #
    botoncontinuar = tk.Button(canvaprincipal, text= 'Continuar', font= ('Benguiat Bold', 12), command = lambda: continuar1()) #Crea un botón que al ser presionado ejecuta la función 'modos'
    botoncontinuar.place(x= 371, y= 500, anchor="center") #Posiciona el botón en el canva

    def continuar1():
        if username1.get() != '' or username2.get() != '': #Si el campo de texto no está vacío
            modos() #Ejecuta la función 'modos'

        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre de usuario") #Si el campo de texto está vacío, muestra un mensaje de advertencia


def modos():
    canvaprincipal.delete("all")
    username1.destroy() #Elimina el campo de texto
    username2.destroy() #Elimina el campo de texto
    botoncontinuar.destroy() #Elimina el botón

    canvaprincipal.create_text(371, 120, text= 'Modos de juego', fill= '#D7271E' , font= ('Stranger Things Outlined', 55))

    canvaprincipal.create_rectangle(50, 150, 300, 250, outline='white') #Crea un rectángulo para el primer modo de juego
    canvaprincipal.create_rectangle(450, 150, 700, 250, outline='white') #Crea un rectángulo para el segundo modo de juego

    canvaprincipal.create_text(171, 230, text= 'Escucha y transmición', fill= 'white' , font= ('Benguiat Bold', 15))
    canvaprincipal.create_text(571, 230, text= 'Transmisión simple', fill= 'white' , font= ('Benguiat Bold', 15))




ventprincipal.bind("<Key>", continuar) #Al tocar cualquier tecla se ejecuta 'continuar'

parpadear() #Ejecuta 'parpadear'

canvaprincipal.pack()

ventprincipal.mainloop()