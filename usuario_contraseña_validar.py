import tkinter as tk  # Para interfaces gráficas
from tkinter import messagebox  # Para mostrar mensajes emergentes

import bcrypt  # Para manejar el hash de contraseñas y su validación


# Función que se ejecuta cuando el usuario intenta validar su contraseña
def validar_contraseña():
    # Obtenemos el texto que ha sido ingresado en los campos de usuario y contraseña
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # nuestra contraseña (según la profe, esto tendría que estar en una base de datos)
    contraseña_correcta = "pass1234"

    # Hash de la contraseña correcta usando bcrypt.
    hashed = bcrypt.hashpw(contraseña_correcta.encode('utf-8'), bcrypt.gensalt())

    # Verificamos si la contraseña ingresada por el usuario coincide con la contraseña correcta hasheada previamente
    if bcrypt.checkpw(contraseña.encode('utf-8'), hashed):
        # Si la contraseña es correcta
        messagebox.showinfo("Éxito", f"Bienvenido {usuario}!")
    else:
        # Si la contraseña es incorrecta
        messagebox.showerror("Error", "Contraseña incorrecta")


if __name__ == '__main__':
    # Crea la ventana principal de la aplicación
    root = tk.Tk()
    root.title("Autenticación de Usuario")  # Eso sería el título de nuestra ventana

    root.geometry("1000x500")  # Dimensiones de la ventana

    # Creamos una etiqueta (texto que aparecerá) para el campo de usuario
    label_usuario = tk.Label(root, text="Usuario:")
    label_usuario.pack(pady=5)  # Mostramos con pack la etiqueta y le damos un pequeño espacio vertical

    # Creamos un campo de entrada donde el usuario pueda escribir su nombre de usuario
    entry_usuario = tk.Entry(root)
    entry_usuario.pack(pady=5)  # Mostramos el campo de entrada con pack

    # Creamos una etiqueta para el campo de contraseña
    label_contraseña = tk.Label(root, text="Contraseña:")
    label_contraseña.pack(pady=5)

    # Creamos un campo de entrada para la contraseña.
    # show="*" hace que se oculta el texto mientras escribimos
    entry_contraseña = tk.Entry(root, show="*")
    entry_contraseña.pack(pady=5)

    # Crear un botón que, cuando se hace clic, llama a la función validar_contraseña()
    btn_validar = tk.Button(root, text="Validar", command=validar_contraseña)
    btn_validar.pack(pady=20)  # Mostramos con pack el botón y le damos un espacio vertical

    # Esta línea muestra la ventana y espera a que el usuario interactúe con ella
    root.mainloop()
