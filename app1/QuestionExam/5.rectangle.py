import unittest

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def calculer_surface(self):
        return self.longueur * self.largeur

class TestRectangle(unittest.TestCase):

    def test_calculer_perimetre(self):
        rectangle = Rectangle(4, 5)
        perimetre = rectangle.calculer_perimetre()
        print(f"Périmètre du rectangle : {perimetre}")
        self.assertEqual(perimetre, 18)

    def test_calculer_surface(self):
        rectangle = Rectangle(4, 5)
        surface = rectangle.calculer_surface()
        print(f"Surface du rectangle : {surface}")
        self.assertEqual(surface, 20)

if __name__ == '__main__':
    unittest.main()
