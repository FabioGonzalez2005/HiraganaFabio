import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import random

traducciones = {}
aciertos = 0
indice_actual = 0

def cargar_imagenes():
    imagenes = os.listdir("hiragana")
    return random.sample(imagenes, 10)

imagenes = cargar_imagenes()

def comprobar_traduccion():
    respuesta = entrada.get().lower()
    if respuesta == traducciones[indice_actual]:
        global aciertos
        aciertos += 1
    siguiente_imagen()

def siguiente_imagen():
    global indice_actual
    indice_actual += 1
    if indice_actual < len(imagenes):
        cargar_y_mostrar_imagen(indice_actual)
        entrada.delete(0, tk.END)
    else:
        mostrar_resultado()

def mostrar_resultado():
    calificacion = aciertos
    v2 = tk.Toplevel(root)
    v2.title("Hiragana de Fabio")

    if calificacion < 5:
        mensaje = f"Nos vemos en septiembre crack. Sacaste un {calificacion}. Te pondré un suspenso."
        imagen_suspenso = Image.open('suspenso.jpg')
        imagen_suspenso = imagen_suspenso.resize((200, 280))
        foto_suspenso = ImageTk.PhotoImage(imagen_suspenso)

        label_suspenso = tk.Label(v2, image=foto_suspenso)
        label_suspenso.image = foto_suspenso
        label_suspenso.pack(pady=10)

    elif calificacion == 5:
        mensaje = f"5 Pelao, ¿no lo habrás hecho al azar no? Tu calificación es: {calificacion}, te pondré un suficiente."
        imagen_suficiente = Image.open('suficiente.jpg')
        imagen_suficiente = imagen_suficiente.resize((200, 200))
        foto_suficiente = ImageTk.PhotoImage(imagen_suficiente)

        label_suficiente = tk.Label(v2, image=foto_suficiente)
        label_suficiente.image = foto_suficiente
        label_suficiente.pack(pady=10)
    elif calificacion == 6:
        mensaje = f"Sigue así bestia, o notita pa casita, {calificacion}, te pondré un bien."
        imagen_bien = Image.open('bien.jpg')
        imagen_bien = imagen_bien.resize((280, 200))
        foto_bien = ImageTk.PhotoImage(imagen_bien)

        label_bien = tk.Label(v2, image=foto_bien)
        label_bien.image = foto_bien
        label_bien.pack(pady=10)

    elif calificacion >= 7 and calificacion < 9:
        mensaje = f"Oye bien crack. Sacaste un {calificacion}, te pondré un notable."
        imagen_notable = Image.open('notable.jpg')
        imagen_notable = imagen_notable.resize((200, 270))
        foto_notable = ImageTk.PhotoImage(imagen_notable)

        label_notable = tk.Label(v2, image=foto_notable)
        label_notable.image = foto_notable
        label_notable.pack(pady=10)
    else:
        mensaje = f"El duolingo te tiene miedo chaval. Sacaste un {calificacion}, te pondré un sobresaliente."
        imagen_sobresaliente = Image.open('sobresaliente.jpg')
        imagen_sobresaliente = imagen_sobresaliente.resize((280, 200))
        foto_sobresaliente = ImageTk.PhotoImage(imagen_sobresaliente)

        label_sobresaliente = tk.Label(v2, image=foto_sobresaliente)
        label_sobresaliente.image = foto_sobresaliente
        label_sobresaliente.pack(pady=10)

    label_resultado = tk.Label(v2, text=mensaje, padx=20, pady=20)
    label_resultado.pack()

    button_cerrar = tk.Button(v2, text="Cerrar", command=v2.destroy)
    button_cerrar.pack(pady=10)

def cargar_y_mostrar_imagen(indice):
    imagen_path = os.path.join("hiragana", imagenes[indice])
    imagen = Image.open(imagen_path).resize((256, 256))
    foto = ImageTk.PhotoImage(imagen)
    label.config(image=foto)
    label.image = foto
    traduccion_correcta = os.path.splitext(imagenes[indice])[0]
    traducciones[indice] = traduccion_correcta

root = tk.Tk()
root.title("Hiragana de Fabio")

label = ttk.Label(root)
label.pack(pady=10)

entrada = ttk.Entry(root)
entrada.pack(pady=5)

boton_comprobar = ttk.Button(root, text="Comprobar", command=comprobar_traduccion)
boton_comprobar.pack(pady=5)

label_traduccion = ttk.Label(root)
label_traduccion.pack(pady=10)

cargar_y_mostrar_imagen(indice_actual)
root.mainloop()
