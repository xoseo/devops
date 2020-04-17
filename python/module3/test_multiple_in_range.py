import os
import sys
import unittest

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module3.multiple_in_range import multiple_in_range


class TestBetween(unittest.TestCase):

    def test_multiple_in_range(self):
        self.assertEqual(multiple_in_range(1, 77), [7, 14, 21, 28, 42, 49, 56, 63, 77])
        self.assertEqual(multiple_in_range(-77, 77),
                         [-77, -63, -56, -49, -42, -28, -21, -14, -7, 7, 14, 21, 28, 42, 49, 56, 63, 77])
        self.assertEqual(multiple_in_range(-77, -7), [-77, -63, -56, -49, -42, -28, -21, -14, -7])
        with self.assertRaises(TypeError, msg="multiple_in_range(0, 55.55)"):
            multiple_in_range(0, 55.55)
        with self.assertRaises(TypeError, msg='multiple_in_range(0, "")'):
            multiple_in_range(0, "")


if __name__ == "__main__":
    unittest.main()
