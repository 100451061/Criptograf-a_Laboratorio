import unittest
import app  # Importar el archivo app.py que contiene nuestras funciones
import bcrypt
from unittest.mock import patch, mock_open
import json

class TestValidacionContraseña(unittest.TestCase):

    @patch('app.leer_contraseña_desde_json')
    def test_contraseña_correcta(self, mock_leer_contraseña):
        # Simular que la contraseña correcta en el archivo JSON es "1234"
        mock_leer_contraseña.return_value = "1234"
        
        # Verificar que la contraseña correcta pasa la validación
        self.assertTrue(app.validar_contraseña("1234"))

    @patch('app.leer_contraseña_desde_json')
    def test_contraseña_incorrecta(self, mock_leer_contraseña):
        # Simular que la contraseña correcta en el archivo JSON es "1234"
        mock_leer_contraseña.return_value = "1234"
        
        # Verificar que una contraseña incorrecta no pasa la validación
        self.assertFalse(app.validar_contraseña("wrongpassword"))

    @patch('builtins.open', new_callable=mock_open)
    def test_archivo_no_encontrado(self, mock_file):
        # Simular que se lanza un FileNotFoundError cuando se intenta abrir el archivo JSON
        mock_file.side_effect = FileNotFoundError
        
        # Verificar que si el archivo no existe, se lanza un FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            app.leer_contraseña_desde_json()

if __name__ == '__main__':
    unittest.main()
