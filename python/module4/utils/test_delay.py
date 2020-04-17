import unittest
from datetime import datetime
import os
import sys

PACKAGE_PARENT = '../../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module4.utils.delay import delay

class TestDelayDec(unittest.TestCase):
    def setUp(self):
        self.test_string = "My shiny string"

    def tearDown(self):
        pass


    def test_delay(self):
        @delay
        def return_str():
            return self.test_string

        t1 = datetime.now()
        _  = return_str()
        self.assertGreater((datetime.now() - t1).total_seconds(), 3, msg="Run time should be grater that 3 seconds")

    def test_delay_with_doc(self):
        @delay
        def return_str():
            """Test docstring"""
            return self.test_string

        self.assertEqual(return_str.__name__, "return_str", msg="Function name has changed after decoration")
        self.assertEqual(return_str.__doc__, "Test docstring", msg="Docstring name has changed after decoration")

    def test_double_delay(self):
        @delay
        @delay
        def return_str():
            return self.test_string

        t1 = datetime.now()
        _  = return_str()
        print((datetime.now() - t1).total_seconds())
        self.assertGreater((datetime.now() - t1).total_seconds(), 6, msg="Run time should be grater that 6 seconds")


if __name__ == "__main__":
    unittest.main()