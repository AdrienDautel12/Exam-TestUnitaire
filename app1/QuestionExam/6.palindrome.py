import unittest

def est_palindrome(chaine):
    chaine_inverse = chaine[::-1]
    chaine = chaine.lower().replace(" ", "")
    return chaine == chaine_inverse

class TestEstPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        resultat = est_palindrome("radar")
        print("La chaîne 'radar' est un palindrome :", resultat)
        self.assertTrue(resultat)

    def test_palindrome_avec_espaces(self):
        resultat = est_palindrome("A man a plan a canal Panama")
        print("La chaîne 'A man a plan a canal Panama' est un palindrome :", resultat)
        self.assertFalse(resultat)

    def test_palindrome_casse_sensible(self):
        resultat = est_palindrome("Radar")
        print("La chaîne 'Radar' est un palindrome :", resultat)
        self.assertFalse(resultat)

    def test_non_palindrome(self):
        resultat = est_palindrome("hello")
        print("La chaîne 'hello' est un palindrome :", resultat)
        self.assertFalse(resultat)

    def test_chaine_vide(self):
        resultat = est_palindrome("")
        print("La chaîne vide est un palindrome :", resultat)
        self.assertTrue(resultat)

if __name__ == '__main__':
    unittest.main()
