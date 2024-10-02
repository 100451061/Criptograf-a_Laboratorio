import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# cifrado simetrico

# Generar una clave de 256 bits (32 bytes) para AES-256
clave = os.urandom(32)  # Genera una clave aleatoria

# Generar un IV (vector de inicialización) de 16 bytes
iv = os.urandom(16)


# Función para cifrar un mensaje usando AES en modo CBC
def cifrar_mensaje(mensaje, clave, iv):
    # Inicializar el cifrador con AES en modo CBC
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv))

    # Añadir padding al mensaje para que sea múltiplo de 16 bytes (bloque de AES)
    padder = padding.PKCS7(128).padder()  # AES usa bloques de 128 bits (16 bytes)
    mensaje_padded = padder.update(mensaje.encode()) + padder.finalize()

    # Cifrar el mensaje
    cifrador_encryptor = cifrador.encryptor()
    mensaje_cifrado = cifrador_encryptor.update(mensaje_padded) + cifrador_encryptor.finalize()

    return mensaje_cifrado


# Función para descifrar un mensaje usando AES en modo CBC
def descifrar_mensaje(mensaje_cifrado, clave, iv):
    # Inicializar el descifrador con AES en modo CBC
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv))

    # Descifrar el mensaje
    cifrador_decryptor = cifrador.decryptor()
    mensaje_padded = cifrador_decryptor.update(mensaje_cifrado) + cifrador_decryptor.finalize()

    # Eliminar el padding del mensaje descifrado
    unpadder = padding.PKCS7(128).unpadder()
    mensaje_descifrado = unpadder.update(mensaje_padded) + unpadder.finalize()

    return mensaje_descifrado.decode()


# Ejemplo de uso
mensaje_original = "Este es un mensaje secreto."
print(f"Mensaje original: {mensaje_original}")

# Cifrar el mensaje
mensaje_cifrado = cifrar_mensaje(mensaje_original, clave, iv)
print(f"Mensaje cifrado (hex): {mensaje_cifrado.hex()}")

# Descifrar el mensaje
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave, iv)
print(f"Mensaje descifrado: {mensaje_descifrado}")
