### Buenas Prácticas de programación con Python
### Alumna: María del Rocío Roldán de la Rosa
### 23/05/2023

### ACTIVIDAD LECCIÓN 2 - COMPRENDER LA IMPORTANCIA DEL DESARROLLO GUIADO POR PRUEBAS ###

# Implementa un Script con un conjunto de funciones y crea un mínimo de 5 test para cada 
# una de las librerías de test vistas en la clase (unittest y pytest):

# 1º Creamos un conjunto de funciones simples:
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def es_par(numero):
    return numero % 2 == 0


# Pruebas con Unittest:
## Para ejecutar las pruebas con unittest: python -m unittest actividad_2.py 
## python -m unittest -v

# Librería
import unittest
class TestFunciones(unittest.TestCase):
    
    # Puntual, para cuando queramos pasarle algún valor a la clase (de forma dinámica 
    # o queramos inicializar algo).
    # Método. Se ejecuta antes de cada test 
    #def setUp(self):
    #    print('setUp') # Ejemplo abrir la API
    
    # Método. Se ejecuta al finalizar de cada test 
    #def tearDown(self):
    #    print('tearDown\n') # Ejemplo cerrar la API
        
    def test_sumar(self):
        print("Comenzando suma")
        self.assertEqual(funciones.sumar(2, 3), 5)
        self.assertEqual(funciones.sumar(-5, 10), 5)
        self.assertEqual(funciones.sumar(0, 0), 0)
        
    def test_restar(self):
        print("Comenzando resta")
        self.assertEqual(funciones.restar(5, 3), 2)
        self.assertEqual(funciones.restar(10, -5), 15)
        self.assertEqual(funciones.restar(0, 0), 0)
        
    def test_multiplicar(self):
        print("Comenzando multiplicación")
        self.assertEqual(funciones.multiplicar(2, 3), 6)
        self.assertEqual(funciones.multiplicar(-5, 10), -50)
        self.assertEqual(funciones.multiplicar(0, 5), 0)
        
    def test_dividir(self):
        print("Comenzando división")
        self.assertEqual(funciones.dividir(6, 3), 2)
        self.assertEqual(funciones.dividir(10, -5), -2)
        self.assertRaises(ValueError, funciones.dividir, 6, 0)
    
    def test_es_par(self):
        print("Indica TRUE o FALSE a PAR")
        self.assertTrue(funciones.es_par(2))
        self.assertFalse(funciones.es_par(3))
        self.assertTrue(funciones.es_par(0))
        
if __name__ == '__main__':
    unittest.main()
    
# Pruebas con Pytest:
## Para ejecutar las pruebas con pytest: pytest test_actividad_2_funcion.py

# Librería
from funciones import funciones
import pytest

def test_sumar():
    print("Comenzando suma") 
    assert funciones.sumar(2, 3) == 5
    assert funciones.sumar(-5, 10) == 5
    assert funciones.sumar(0, 0) == 0

def test_restar():
    print("Comenzando resta") 
    assert funciones.restar(5, 3) == 2
    assert funciones.restar(10, -5) == 15
    assert funciones.restar(0, 0) == 0

def test_multiplicar():
    print("Comenzando multiplicación") 
    assert funciones.multiplicar(2, 3) == 6
    assert funciones.multiplicar(-5, 10) == -50
    assert funciones.multiplicar(0, 5) == 0

def test_dividir():
    print("Comenzando división") 
    assert funciones.dividir(6, 3) == 2
    assert funciones.dividir(10, -5) == -2
    with pytest.raises(ValueError):
        funciones.dividir(6, 0)

def test_es_par():
    print("Indica TRUE o FALSE a PAR")
    assert funciones.es_par(2) is True
    assert funciones.es_par(3) is False
    assert funciones.es_par(0) is True

