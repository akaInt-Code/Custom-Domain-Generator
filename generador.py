import os

os.system("pip install tkinter")
os.system("pip install pyperclip")
os.system("cls")

import tkinter as tk
import random
import string
import pyperclip

def generar_correo_contraseña():
    nombre = nombre_entry.get()
    apellidos = apellidos_entry.get()

    primer_nombre = nombre.split()[0].lower()
    primer_apellido = apellidos.split()[0].lower()
    correo = f"{primer_nombre}.{primer_apellido}@domain.help"

    letras_y_numeros = string.ascii_letters + string.digits
    contraseña = "QwertyGR." + ''.join(random.choice(letras_y_numeros) for _ in range(6))

    correo_label.config(text=f"Correo: {correo}")
    contraseña_label.config(text=f"Contraseña: {contraseña}")

    pyperclip.copy(f"Correo: {correo}\nContraseña: {contraseña}")

ventana = tk.Tk()
ventana.title("RI Mails")

input_frame = tk.Frame(ventana)
input_frame.pack(pady=10)

nombre_label = tk.Label(input_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=10, pady=5)
nombre_entry = tk.Entry(input_frame)
nombre_entry.grid(row=0, column=1, padx=10, pady=5)

apellidos_label = tk.Label(input_frame, text="Apellidos:")
apellidos_label.grid(row=1, column=0, padx=10, pady=5)
apellidos_entry = tk.Entry(input_frame)
apellidos_entry.grid(row=1, column=1, padx=10, pady=5)

generar_button = tk.Button(ventana, text="Generar Correo y Contraseña", command=generar_correo_contraseña)
generar_button.pack(pady=5)

resultado_frame = tk.Frame(ventana)
resultado_frame.pack(pady=10)

correo_label = tk.Label(resultado_frame, text="", font=("Arial", 12, "bold"))
correo_label.grid(row=0, column=0, padx=10, pady=5)

contraseña_label = tk.Label(resultado_frame, text="", font=("Arial", 12, "bold"))
contraseña_label.grid(row=1, column=0, padx=10, pady=5)

copiar_button = tk.Button(ventana, text="Copiar al Portapapeles", command=lambda: pyperclip.copy(correo_label.cget("text") + "\n" + contraseña_label.cget("text")))
copiar_button.pack(pady=5)

ventana.mainloop()

# by akaint