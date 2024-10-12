import unittest
from number_representations import to_roman_numeral

class test_to_roman_numeral(unittest.TestCase):
    def test_smaller_numbers(self):
        self.assertEqual(to_roman_numeral(9),'IX')
        self.assertEqual(to_roman_numeral(4),'IV')
        self.assertEqual(to_roman_numeral(6),'VI')
        
    def test_larger_number(self):
        self.assertEqual(to_roman_numeral(44), 'XLIV')
        self.assertEqual(to_roman_numeral(1343), 'MCCCXLIII')
        self.assertEqual(to_roman_numeral(99), 'XCIX')
        self.assertEqual(to_roman_numeral(34388), '')
        self.assertEqual(to_roman_numeral(900), 'CM')
        self.assertEqual(to_roman_numeral(400), 'CD')
        self.assertEqual(to_roman_numeral(999), 'CMXCIX')
