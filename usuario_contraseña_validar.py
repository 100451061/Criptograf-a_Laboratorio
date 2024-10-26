import json
import os
import sys
import tkinter as tk  # Para interfaces gráficas
from tkinter import messagebox

import bcrypt  # Para manejar el hash de contraseñas y su validación

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Función para leer la contraseña desde un archivo JSON
def leer_contraseña_desde_archivo():
    try:
        # Ruta absoluta o relativa al archivo JSON
        ruta_absoluta = os.path.abspath("contraseña.json")
        print(f"Buscando el archivo en: {ruta_absoluta}")
        # Cargar el contenido del archivo JSON
        with open("contraseña.json", "r") as file:
            data = json.load(file)
            return data["contraseña_correcta"]  # Retornar el valor de la contraseña
    except FileNotFoundError:
        # Mostrar mensaje de error si el archivo no se encuentra
        messagebox.showerror("Error", "No se encontró el archivo de la contraseña.")
    except KeyError:
        # Mostrar mensaje de error si no existe la clave correcta en el JSON
        messagebox.showerror("Error", "La clave 'contraseña_correcta' no se encuentra en el archivo JSON.")


# Función que se ejecuta cuando el usuario intenta validar su contraseña
def validar_contraseña():
    # Obtenemos el texto que ha sido ingresado en los campos de usuario y contraseña
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Validar que el campo de usuario no esté vacío  (Obligatorio)
    # (Si el campo está vacío, se muestra un mensaje de error y no se realiza ninguna otra acción.)
    if not usuario:
        messagebox.showerror("Error", "El campo de usuario no puede estar vacío.")
        return None

    # Leer la contraseña correcta desde el archivo JSON
    contraseña_correcta = leer_contraseña_desde_archivo()

    if not contraseña_correcta:
        return None  # Si no se puede leer la contraseña, salir de la función

    # Hash de la contraseña correcta usando bcrypt
    hashed = bcrypt.hashpw(contraseña_correcta.encode('utf-8'), bcrypt.gensalt())

    # Verificamos si la contraseña ingresada por el usuario coincide con la correcta
    if bcrypt.checkpw(contraseña.encode('utf-8'), hashed):
        # Si la contraseña es correcta
        messagebox.showinfo("Éxito", f"Bienvenido {usuario}!")
    else:
        # Si la contraseña es incorrecta
        messagebox.showerror("Error", "Contraseña incorrecta")


if __name__ == '__main__':
    # Crear la ventana principal de la aplicación
    root = tk.Tk()
    root.title("Autenticación de Usuario")  # Título de la ventana

    root.geometry("1000x500")  # Dimensiones de la ventana

    # Crear etiqueta para el nombre de usuario
    label_usuario = tk.Label(root, text="Usuario:")
    label_usuario.pack(pady=5)  # Mostrar la etiqueta con espacio vertical

    # Crear campo de entrada para el usuario
    entry_usuario = tk.Entry(root)
    entry_usuario.pack(pady=5)

    # Crear etiqueta para la contraseña
    label_contraseña = tk.Label(root, text="Contraseña:")
    label_contraseña.pack(pady=5)

    # Crear campo de entrada para la contraseña con ocultación de caracteres
    entry_contraseña = tk.Entry(root, show="*")
    entry_contraseña.pack(pady=5)

    # Crear botón para validar la contraseña
    btn_validar = tk.Button(root, text="Validar", command=validar_contraseña)
    btn_validar.pack(pady=20)

    # Iniciar el loop de la ventana
    root.mainloop()
