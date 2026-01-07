import unittest

class MiPrueba(unittest.TestCase):
    
    def setUp(self):
        '''Este método se ejecuta antes de cada prueba'''
        self.dato1 = 10
        self.dato2 = 5

    def test_suma(self):
        '''Verifica la suma de dos números'''
        resultado = self.dato1 + self.dato2
        self.assertEqual(resultado, 16)

    def test_resta(self):
        '''Verifica la resta de dos números'''
        resultado = self.dato1 - self.dato2
        self.assertEqual(resultado, 5)

    def test_multiplicacion(self):
        '''Verifica la multiplicación de dos números'''
        resultado = self.dato1 * self.dato2
        self.assertEqual(resultado, 50)

    def test_division(self):
        '''Verifica la división de dos números'''
        resultado = self.dato1 / self.dato2
        self.assertEqual(resultado, 2)

    def tearDown(self):
        '''Este método se ejecuta después de cada prueba'''
        del self.dato1
        del self.dato2

if __name__ == '__main__':
    unittest.main()
