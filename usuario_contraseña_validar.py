import tkinter as tk
from tkinter import messagebox

import bcrypt

# Comentario

# Crear ventana principal
root = tk.Tk()
root.title("Autenticación de Usuario")

# Dimensiones de la ventana
root.geometry("1000x500")


# Función para validar la contraseña
def validar_contrasena():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Hasheado simulado de la contraseña correcta
    contrasena_correcta = "pass1234"
    hashed = bcrypt.hashpw(contrasena_correcta.encode('utf-8'), bcrypt.gensalt())

    # Verificar si la contraseña ingresada es válida
    if bcrypt.checkpw(contrasena.encode('utf-8'), hashed):
        messagebox.showinfo("Éxito", f"Bienvenido {usuario}!")
    else:
        messagebox.showerror("Error", "Contraseña incorrecta")


if __name__ == '__main__':
    # Etiqueta y campo para el nombre de usuario
    label_usuario = tk.Label(root, text="Usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(root)
    entry_usuario.pack(pady=5)

    # Etiqueta y campo para la contraseña
    label_contrasena = tk.Label(root, text="Contraseña:")
    label_contrasena.pack(pady=5)
    entry_contrasena = tk.Entry(root, show="*")  # Ocultar la contraseña con '*'
    entry_contrasena.pack(pady=5)

    # Botón para validar la contraseña
    btn_validar = tk.Button(root, text="Validar", command=validar_contrasena)
    btn_validar.pack(pady=20)

    # Ejecutar la ventana
    root.mainloop()
