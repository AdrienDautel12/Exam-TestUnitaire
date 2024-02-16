import unittest

def calculer_moyenne(liste):
    if len(liste) == 0:
        raise ValueError("La liste est vide")
    return sum(liste) / len(liste)

class TestCalculerMoyenne(unittest.TestCase):

    def test_liste_non_vide(self):
        liste = [1, 2, 3, 4, 5]
        resultat = calculer_moyenne(liste)
        print(f"La moyenne de la liste {liste} est : {resultat}")
        self.assertEqual(resultat, 3.0)

    def test_liste_vide(self):
        liste = []
        with self.assertRaises(ValueError):
            calculer_moyenne(liste)
        print("Test liste vide")

if __name__ == '__main__':
    unittest.main()
