import unittest

class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

    def obtenir_solde(self):
        return self.solde

class TestCompteBancaire(unittest.TestCase):

    def test_deposer(self):
        compte = CompteBancaire(100)
        montant_depose = 50
        compte.deposer(montant_depose)
        print(f"Dépôt de {montant_depose} €, Nouveau solde : {compte.obtenir_solde()} €")
        self.assertEqual(compte.obtenir_solde(), 150)

    def test_retirer(self):
        compte = CompteBancaire(100)
        montant_retire = 50
        compte.retirer(montant_retire)
        print(f"Retrait de {montant_retire} € , Nouveau solde : {compte.obtenir_solde()} €")
        self.assertEqual(compte.obtenir_solde(), 50)

    def test_obtenir_solde(self):
        compte = CompteBancaire(100)
        print(f"Solde actuel : {compte.obtenir_solde()} €")
        self.assertEqual(compte.obtenir_solde(), 100)

    def test_retirer_solde_insuffisant(self):
        compte = CompteBancaire(100)
        montant_retire = 150
        with self.assertRaises(ValueError):
            compte.retirer(montant_retire)
        print("Solde insuffisant, Annulée.")
        self.assertEqual(compte.obtenir_solde(), 100)

if __name__ == '__main__':
    unittest.main()
