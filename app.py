import bcrypt
import json

# Función para leer la contraseña desde un archivo JSON
def leer_contraseña_desde_json():
    try:
        with open("contraseña.json", "r") as file:
            data = json.load(file)  # Cargar el contenido del archivo JSON
            return data["contraseña_correcta"]  # Retornar el valor de la contraseña
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo JSON de la contraseña.")
    except KeyError:
        raise KeyError("La clave 'contraseña_correcta' no se encuentra en el archivo JSON.")


# Función que valida la contraseña ingresada por el usuario
def validar_contraseña(contraseña):
    contraseña_correcta = leer_contraseña_desde_json()

    # Hashear la contraseña correcta para simular la verificación
    hashed = bcrypt.hashpw(contraseña_correcta.encode('utf-8'), bcrypt.gensalt())

    # Verificar si la contraseña ingresada coincide con la correcta
    return bcrypt.checkpw(contraseña.encode('utf-8'), hashed)
