import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

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

    global nombre1, nombre2, botoncontinuar

    canvaprincipal.create_text(371, 310, text= 'Jugador 1', fill= 'white' , font= ('Benguiat Bold', 12)) #Crea el texto que indica el campo de texto para el jugador 1
    nombre1 = tk.Entry(canvaprincipal, font= ('Benguiat Bold', 12), fg= 'white', background= 'black', insertbackground= 'white', highlightbackground= '#D7271E', highlightthickness = 2, relief= 'solid', justify= 'center') #Crea un campo de texto para que el usuario escriba su nombre de usuario
    nombre1.place(x= 371, y= 350, anchor="center") #Posiciona el campo de texto en el canva

    canvaprincipal.create_text(371, 390, text= 'Jugador 2', fill= 'white' , font= ('Benguiat Bold', 12)) #Crea el texto que indica el campo de texto para el jugador 2
    nombre2 = tk.Entry(canvaprincipal, font= ('Benguiat Bold', 12), fg= 'white', background= 'black', insertbackground= 'white', highlightbackground= '#D7271E', highlightthickness = 2, relief= 'solid', justify= 'center') #Crea un campo de texto para que el usuario escriba su nombre de usuario
    nombre2.place(x= 371, y= 430, anchor="center") #
    botoncontinuar = tk.Button(canvaprincipal, text= 'Continuar', font= ('Retro Gaming', 12, 'bold'), command = lambda: continuar1(), bg = '#D7271E', fg = 'black', activebackground= "#B82119", bd = 0 ) #Crea un botón que al ser presionado ejecuta la función 'modos'
    botoncontinuar.place(x= 371, y= 500, anchor="center") #Posiciona el botón en el canva

    def continuar1():
        if nombre1.get() != '' and nombre2.get() != '': #Si el campo de texto no está vacío
            elegir_modos() #Ejecuta la función 'modos'

        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre de usuario") #Si el campo de texto está vacío, muestra un mensaje de advertencia


def elegir_modos():
    canvaprincipal.delete("all")
    nombre1.destroy() #Elimina el campo de texto
    nombre2.destroy() #Elimina el campo de texto
    botoncontinuar.destroy() #Elimina el botón

    canvaprincipal.create_text(371, 120, text= 'Modos de juego', fill= '#D7271E' , font= ('Stranger Things Outlined', 55))

    canvaprincipal.create_rectangle(15, 190, 350, 650, outline='white')
    canvaprincipal.create_rectangle(390, 190, 727, 650, outline='white')

    canvaprincipal.create_text(183, 230, text= 'Escucha y transmisión', fill= 'white' , font= ('Benguiat Bold', 15))
    canvaprincipal.create_text(183, 365, text= '• Dos personas deben interpretar una frase transmitida por luces o sonidos desde la maqueta. \n'
    ' \n '
    '• En cada ronda el jugador 1 usa el teclado de la computadora y el jugador 2, los botones físicos de la maqueta para ingresar su respuesta. \n'
    ' \n '
    '• Los participantes intercambian sus puestos para repetir el proceso con la misma frase', fill= 'white' , font= ('Benguiat Bold', 9), width = 270)
    canvaprincipal.create_text(559, 230, text= 'Transmisión simple', fill= 'white' , font= ('Benguiat Bold', 15))
    canvaprincipal.create_text(559, 365, text= '• Desde la maqueta, los jugadores transmiten un mensaje previamente seleccionado para que sea recibido en la computadora.  \n'
    ' \n '
    '• Se validará el mensaje y se asignará un puntaje según la velocidad de transmisión y el acierto de caracteres.  \n'
    ' \n '
    '• Al final de cada ronda, se cambia de turno hasta encontrar un ganador', fill= 'white', font= ('Benguiat Bold', 9), width = 270)

    global boton_et, boton_ts

    boton_et = tk.Button(canvaprincipal, text= 'Elegir modo', font= ('Retro Gaming', 12, 'bold'), bg= '#D7271E', fg= 'black', activebackground= '#B82119', bd= 0, command= lambda: modo_et())
    boton_et.place(x= 183, y= 610, anchor= 'center')
    boton_ts = tk.Button(canvaprincipal, text= 'Elegir modo', font= ('Retro Gaming', 12, 'bold'), bg= '#D7271E', fg= 'black', activebackground= '#B82119', bd= 0, command= lambda: modo_ts())
    boton_ts.place(x= 559, y= 610, anchor= 'center' )


frases = [
    'SOS',
    'RADIO',
    'VOLTAJE +220',
    'YES',
    'NO',
    'SALDO -10',
    'SUBMARINO',
    'TRANSMISIÓN OK',
    'WHISKY',
    'STRANGERTEC',
]

frase_actual = ''


def rondas():
    global frase_actual

    frases_disponibles = [f for f in frases if f != frase_actual]

    if frases_disponibles:
        frase_actual = random.choice(frases_disponibles)
    
    else:
        frase_actual = random.choice(frases)


Morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '+': '.-.-.', '-': '-....-'
} #Diccionario para convertir de texto a código Morse

Morse_Inv = {v: k for k, v in Morse.items()} #Diccionario para invertir de código Morse a texto


def modo_et():
    canvaprincipal.delete('all')
    boton_ts.destroy()
    boton_et.destroy()

    canvaprincipal.create_text(371, 100, text= 'Escucha y Transmision', fill= '#D7271E' , font= ('Stranger Things Outlined', 43), justify= 'center')
    canvaprincipal.create_text(371, 200, text= 'Frase a transmitir:', fill= 'white' , font= ('Benguiat Bold', 15), justify= 'center')
    texto_frase = canvaprincipal.create_text(371, 300, text= '', fill= 'white', font= ('Retro Gaming', 20), justify= 'center')
    canvaprincipal.itemconfig(texto_frase, text= frase_actual)
    

def modo_ts():
    canvaprincipal.delete('all')
    boton_ts.destroy()
    boton_et.destroy()


ventprincipal.bind("<Key>", continuar) #Al tocar cualquier tecla se ejecuta 'continuar'

rondas()

parpadear() #Ejecuta 'parpadear'

canvaprincipal.pack()

ventprincipal.mainloop()