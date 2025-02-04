import unittest
from typing import List

def count_long_first_names(first_names: List[str]) -> int:
    """
    Count first_names with more than seven letters.
    """
    max_first_names_length = 7  # Définition d'une constante
    long_first_names_count = sum(1 for first_name in first_names if len(first_name) > max_first_names_length)

    """
    Print result
    """
    for first_name in first_names:
        length_status = "supérieur" if len(first_name) > max_first_names_length else "inférieur ou égal"
        print(f"{first_name} est un prénom avec un nombre de lettres {length_status} à {max_first_names_length}")
    
    return long_first_names_count

"""
Unit testing
"""
class TestCountLongFirstNames(unittest.TestCase):
    def test_count_long_first_names(self):
        first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(count_long_first_names(first_names), 4)

if __name__ == "__main__":
    unittest.main()