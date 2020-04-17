import os
import unittest
import sys

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module3.lists_2_dict import lists_2_dict


class TestLists2Dict(unittest.TestCase):

    def test_lists_2_dict(self):
        self.assertEqual(lists_2_dict(["Name", "Age", "Job Title"], ["Jane", 44, "Python Developer"]),
                         {"Name": "Jane", "Age": 44, "Job Title": "Python Developer"})

        with self.assertRaises(TypeError, msg=""):
            lists_2_dict(["Name", "Age", {77.2, }], ["Jane", 44, "Python Developer"])


if __name__ == "__main__":
    unittest.main()
