import unittest

"""
Count names with more than seven letters
"""
def compter_nombre_de_lettre_prenoms(prenoms):
    prenom_plus_de_sept = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            prenom_plus_de_sept += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return prenom_plus_de_sept

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        prenom_plus_de_sept = compter_nombre_de_lettre_prenoms(prenoms=prenoms)
        self.assertEqual(prenom_plus_de_sept, 4)

if __name__ == '__main__':
    unittest.main()