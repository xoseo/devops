import unittest
import os
import sys

PACKAGE_PARENT = '../../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module4.utils.raises import raises

class MyCustomException(Exception):
    """My custom exception message"""
    pass

class TestRaisesDec(unittest.TestCase):
    def setUp(self):
        self.test_string = "My shiny string"

    def tearDown(self):
        pass

    def test_raises(self):
        @raises(MyCustomException)
        def return_str():
            return self.test_string + 7

        with self.assertRaises(MyCustomException):
            return_str()

        @raises(MyCustomException)
        def return_str():
            return self.test_string

        try:
            return_str()

        except MyCustomException:
            self.fail(msg="Raises exception in clean code. Shoud replace exception only if it occured.")


if __name__ == "__main__":
    unittest.main()
