import tkinter as tk

ventprincipal = tk.Tk() #Crea la ventana principal
ventprincipal.title("Proyecto StrangerTEC") #El título de la ventana
ventprincipal.geometry("750x750") #Ajusta el tamaño de la ventana
ventprincipal.resizable(width=False, height=False) #Hace que el usuario no pueda cambiar las dimensiones de la ventana

canvaprincipal = tk.Canvas(ventprincipal, width= 742, height= 742, bg= "black") #Crea el canva (donde se coloca el tecto, botones, etc)

canvaprincipal.create_text(371, 310, text= 'Stranger', fill= '#D7271E' , font= ('Stranger Things Outlined', 70)) #Crea el texto que aparece en la ventana
canvaprincipal.create_text(371, 380, text= 'TEC', fill= '#D7271E' , font= ('Stranger Things Outlined', 67))
canvaprincipal.create_text(65, 722, text= 'Jocsan Calvo', fill= 'white' , font= ('Benguiat Bold', 10))
canvaprincipal.create_text(672, 722, text= 'Fabricio Guillén', fill= 'white' , font= ('Benguiat Bold', 10))
text = canvaprincipal.create_text(371, 500, text= '', fill = 'white' , font= ('Benguiat Bold', 12)) #Variable para que el texto pueda parpadear


#Función para que el texto indicado parpadee cada cierto tiempo
def parpadear():
    mtexto = canvaprincipal.itemcget(text, 'text') #Obtiene el texto que contiene la variable text
    
    if mtexto == '':
        canvaprincipal.itemconfig(text, text= 'Presione cualquier tecla para continuar') #Si no hay texto, escribe el mensaje indicado

    else:
        canvaprincipal.itemconfig(text, text= '') #Si ya hay texto, borra el mensaje indicado
    
    ventprincipal.after(750, parpadear) #Hace que la función se ejecute cada 750 milisegundos

parpadear()

canvaprincipal.pack()

ventprincipal.mainloop()