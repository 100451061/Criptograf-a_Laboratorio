# test_validar_contraseña.py

import unittest

from usuario_contraseña_validar import validar_contraseña


class TestValidarContraseña(unittest.TestCase):

    def test_usuario_vacio(self):
        resultado = validar_contraseña("", "1234")
        self.assertEqual(resultado, "El campo de usuario no puede estar vacío.")

    def test_contraseña_vacia(self):
        resultado = validar_contraseña("usuario", "")
        self.assertEqual(resultado, "El campo de contraseña no puede estar vacío.")

    def test_contraseña_correcta(self):
        resultado = validar_contraseña("usuario", "1234")
        self.assertTrue("Bienvenido" in resultado)

    def test_contraseña_incorrecta(self):
        resultado = validar_contraseña("usuario", "incorrecta")
        self.assertEqual(resultado, "Contraseña incorrecta.")


if __name__ == '__main__':
    unittest.main()
