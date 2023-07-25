import tkinter as tk
from PIL import ImageTk, Image

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tour por Salta")

# Crear etiqueta para la imagen
imagen = Image.open("C:/Users/cetrogar/Desktop/usb/imagenes para poryecto/panda.png")
imagen = imagen.resize((600, 600), Image.BILINEAR)
imagen = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(ventana, image=imagen)
imagen_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Calcular el centro de la imagen
centro_x = imagen.width() // 2
centro_y = imagen.height() // 2

# Crear botón para entrar
entrar_button = tk.Button(ventana, text="Entrar", command=lambda: resultado_label.config(text="Bienvenido al Tour por Salta"))
entrar_button.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Crear etiqueta para el resultado de entrar
resultado_label = tk.Label(ventana)
resultado_label.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

# Alinear los widgets hacia la izquierda
for column in range(2):
    ventana.grid_columnconfigure(column, weight=1)


# Iniciar loop principal de la ventana
ventana.mainloop()