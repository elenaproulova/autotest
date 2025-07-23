import unittest
from main import modulo

class TestMath(unittest.TestCase):
    def test_modulo(self):
       self.assertEqual(modulo(5, 2), 1)
       self.assertEqual(modulo(20, 6), 2)
       self.assertEqual(modulo(67, 3), 2)
       self.assertEqual(modulo(125, 3), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, modulo, 16, 0)


if __name__ == '__main__':
   unittest.main()
