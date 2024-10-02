import bcrypt

# Función para leer la contraseña desde un archivo
def leer_contraseña_desde_archivo():
    try:
        with open("contraseña.txt", "r") as file:
            return file.read().strip()  # Leemos el archivo y eliminamos posibles saltos de línea
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo de la contraseña.")

# Función que valida la contraseña ingresada por el usuario
def validar_contraseña(contraseña):
    contraseña_correcta = leer_contraseña_desde_archivo()

    # Hashear la contraseña correcta para simular la verificación
    hashed = bcrypt.hashpw(contraseña_correcta.encode('utf-8'), bcrypt.gensalt())

    # Verificar si la contraseña ingresada coincide con la correcta
    return bcrypt.checkpw(contraseña.encode('utf-8'), hashed)
