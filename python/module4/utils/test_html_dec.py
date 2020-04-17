import unittest
import os
import sys

PACKAGE_PARENT = '../../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module4.utils.html_dec import italic, bold, underline

class TestHtmlDec(unittest.TestCase):
    def setUp(self):
        self.test_string = "My shiny string"

    def tearDown(self):
        pass

    def test_italic(self):
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i>{self.test_string}</i>')

    def test_bold(self):
        @bold
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<b>{self.test_string}</b>')

    def test_underline(self):
        @underline
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<u>{self.test_string}</u>')

    def test_mixed(self):
        @italic
        @bold
        @underline
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i><b><u>{self.test_string}</u></b></i>')

        @bold
        @italic
        @underline
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<b><i><u>{self.test_string}</u></i></b>')

        @underline
        @bold
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<u><b><i>{self.test_string}</i></b></u>')

    def test_repeat(self):
        @italic
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i><i>{self.test_string}</i></i>')

        @italic
        @bold
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i><b><i>{self.test_string}</i></b></i>')


if __name__ == "__main__":
    unittest.main()