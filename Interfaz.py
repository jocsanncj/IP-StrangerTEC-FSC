import tkinter as tk

ventprincipal = tk.Tk()
ventprincipal.title("Proyecto StrangerTEC")
ventprincipal.geometry("750x750")
ventprincipal.resizable(width=False, height=False)

canvaprincipal = tk.Canvas(ventprincipal, width= 742, height= 742, bg= "black")
canvaprincipal.create_text(371, 300, text= 'Stranger', fill= '#D7271E' , font=('Stranger Things Outlined', 60))
canvaprincipal.create_text(371, 360, text= 'TEC', fill= '#D7271E' , font=('Stranger Things Outlined', 57))
canvaprincipal.pack()

ventprincipal.mainloop()