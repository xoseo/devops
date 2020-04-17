import os
import sys
import unittest

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module3.search_in_dict import search_in_dict


class TestBetween(unittest.TestCase):

    def test_search(self):
        haystack = {str(x): x * 2 for x in reversed(range(1000000))}
        self.assertEqual(search_in_dict(["1", "2", "1000", "testStr"], haystack), {"1", "2", "1000"})
        self.assertEqual(search_in_dict({"1", "2", "1000", "testStr"}, haystack), {"1", "2", "1000"})

        with self.assertRaises(TypeError):
            search_in_dict({"1", "2", "1000", {}}, haystack)


if __name__ == "__main__":
    unittest.main()
