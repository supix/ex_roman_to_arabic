import unittest

from main import convert_roman_to_arabic

class MyTestCase(unittest.TestCase):

    def test_trailing_A_is_recognized_as_an_invalid_symbol(self):
        with self.assertRaises(ValueError):
            convert_roman_to_arabic('XIIIA')

    def test_leading_B_is_recognized_as_an_invalid_symbol(self):
        with self.assertRaises(ValueError):
            convert_roman_to_arabic('BXX')

    def test_mid_F_is_recognized_as_an_invalid_symbol(self):
        with self.assertRaises(ValueError):
            convert_roman_to_arabic('XFX')

    def test_space_is_recognized_as_an_invalid_symbol(self):
        with self.assertRaises(ValueError):
            convert_roman_to_arabic('X X')

    def test_XIII_is_13(self):
        self.assertEqual(convert_roman_to_arabic('XIII'), '13')


    def test_MDCLXVI_is_1666(self):
        self.assertEqual(convert_roman_to_arabic('MDCLXVI'), '1666')


    def test_XXI_is_21(self):
        self.assertEqual(convert_roman_to_arabic('XXI'), '21')


    def test_LIX_is_59(self):
        self.assertEqual(convert_roman_to_arabic('LIX'), '59')


    def test_XCI_is_91(self):
        self.assertEqual(convert_roman_to_arabic('XCI'), '91')


    def test_LXXXIX_is_89(self):
        self.assertEqual(convert_roman_to_arabic('LXXXIX'), '89')


    def test_XCV_is_95(self):
        self.assertEqual(convert_roman_to_arabic('XCV'), '95')


    def test_LXXXIV_is_84(self):
        self.assertEqual(convert_roman_to_arabic('LXXXIV'), '84')


    def test_LXIV_is_64(self):
        self.assertEqual(convert_roman_to_arabic('LXIV'), '64')


    def test_C_is_100(self):
        self.assertEqual(convert_roman_to_arabic('C'), '100')


    def test_LXX_is_70(self):
        self.assertEqual(convert_roman_to_arabic('LXX'), '70')


    def test_XIV_is_14(self):
        self.assertEqual(convert_roman_to_arabic('XIV'), '14')


    def test_LXIX_is_69(self):
        self.assertEqual(convert_roman_to_arabic('LXIX'), '69')


    def test_XCVIII_is_98(self):
        self.assertEqual(convert_roman_to_arabic('XCVIII'), '98')


    def test_CIX_is_109(self):
        self.assertEqual(convert_roman_to_arabic('CIX'), '109')


    def test_DCCLXXXVI_is_786(self):
        self.assertEqual(convert_roman_to_arabic('DCCLXXXVI'), '786')


    def test_MCCXCVIII_is_1298(self):
        self.assertEqual(convert_roman_to_arabic('MCCXCVIII'), '1298')


    def test_MMXVII_is_2018(self):
        self.assertEqual(convert_roman_to_arabic('MMXVIII'), '2018')


    def test_MCMLXXXIV_is_1984(self):
        self.assertEqual(convert_roman_to_arabic('MCMLXXXIV'), '1984')


if __name__ == '__main__':
    unittest.main()