import os

from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

"""Utiliza el esquema de cifrado autenticado ChaCha20Poly1305 para cifrar y luego descifrar un mensaje"""
"""ChaCha20Poly1305, AES-GCM, y AES-CCM."""

# Generar una clave de 32 bytes para ChaCha20Poly1305
key = ChaCha20Poly1305.generate_key()

# Crear un objeto de cifrado ChaCha20Poly1305 con la clave generada
chacha = ChaCha20Poly1305(key)

# Generar un nonce de 12 bytes (tamaño estándar para ChaCha20Poly1305)
nonce = os.urandom(12)

# Datos que queremos cifrar
data = b"Este es un mensaje secreto."

# Datos asociados que no serán cifrados, pero cuya integridad será autenticada
aad = b"datos autenticados pero no cifrados"

# Cifrar el mensaje
ciphertext = chacha.encrypt(nonce, data, aad)

# Mostrar el mensaje cifrado
print(f"Mensaje cifrado (hex): {ciphertext.hex()}")

# Descifrar el mensaje, verificando la autenticidad de los datos asociados
try:
    mensaje_descifrado = chacha.decrypt(nonce, ciphertext, aad)
    print(f"Mensaje descifrado: {mensaje_descifrado.decode()}")
except Exception as e:
    print(f"Error al descifrar o verificar la autenticación: {e}")
