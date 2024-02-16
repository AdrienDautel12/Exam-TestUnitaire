import unittest

def compter_mots(phrase):
    mots = phrase.split()
    return len(mots)

class TestCompterMots(unittest.TestCase):

    def test_phrase_vide(self):
        nb_mots = compter_mots("")
        print(f"Vide, Nombre de mots : {nb_mots}")
        self.assertEqual(nb_mots, 0)

    def test_un_mot(self):
        nb_mots = compter_mots("Salut")
        print(f"Un mot, Nombre de mots : {nb_mots}")
        self.assertEqual(nb_mots, 1)

    def test_plusieurs_mots(self):
        nb_mots = compter_mots("Il fait beau")
        print(f"La phrase contient plusieurs mots. Nombre de mots : {nb_mots}")
        self.assertEqual(nb_mots, 3)

if __name__ == '__main__':
    unittest.main()
