import unittest

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

class TestSommeListe(unittest.TestCase):

    def test_liste_melange(self):
        liste = [1, -2, 3, -4, 5]
        resultat = somme_liste(liste)
        print("Liste de nombres mélangés :")
        print(f"Résultat : {resultat}")

    def test_liste_negatifs(self):
        liste = [-1, -2, -3, -4, -5]
        resultat = somme_liste(liste)
        print("Liste de nombres négatifs :")
        print(f"Résultat  : {resultat}")

    def test_liste_positifs(self):
        liste = [1, 2, 3, 4, 5]
        resultat = somme_liste(liste)
        print("Nombres positifs :")
        print(f"Résultat : {resultat}")

    def test_liste_vide(self):
        resultat = somme_liste([])
        print("Test liste vide :")
        print(f"Résultat : {resultat}")
        


    

if __name__ == '__main__':
    unittest.main()
