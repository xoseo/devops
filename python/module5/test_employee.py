import unittest
from unittest import TestCase
import os
import sys

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module5.employee import Employee, Manager, DevOps


class TestEmployee(TestCase):
    def setUp(self):
        self.empl1 = Employee("John", "Doe", 500)
        self.empl2 = Employee("jane", "doe", 300)

    def tearDown(self):
        del self.empl1
        del self.empl2

    def test_full_name(self):
        # Basic props
        self.assertEqual(self.empl1.first_name, 'John')
        self.assertEqual(self.empl1.last_name, 'Doe')
        self.assertEqual(self.empl1.full_name, 'John, Doe')
        self.assertEqual(self.empl1.email, 'john_doe@example.com')
        self.assertEqual(self.empl1.salary, 500)
        self.assertEqual(self.empl2.first_name, 'Jane')
        self.assertEqual(self.empl2.last_name, 'Doe')
        self.assertEqual(self.empl2.full_name, 'Jane, Doe')
        self.assertEqual(self.empl2.email, 'jane_doe@example.com')
        self.assertEqual(self.empl2.salary, 300)

        # full name getter and setter
        self.empl1.full_name = "Homer, Simpson"
        self.empl2.full_name = "bart, simpson"

        msg = "Updating full_name should trigger update for name and last name"

        self.assertEqual(self.empl1.first_name, 'Homer', msg=msg)
        self.assertEqual(self.empl1.last_name, 'Simpson', msg=msg)
        self.assertEqual(self.empl2.first_name, 'Bart', msg=msg)
        self.assertEqual(self.empl2.last_name, 'Simpson', msg=msg)

    def test_from_str(self):
        # @classmethod test
        self.assertEqual(Employee.from_str("John,Doe,500").first_name, self.empl1.first_name)
        self.assertEqual(Employee.from_str("John,Doe,500").last_name, self.empl1.last_name)
        self.assertEqual(Employee.from_str("John,Doe,500").salary, self.empl1.salary)
        self.assertEqual(Employee.from_str("jane,doe,300").first_name, self.empl2.first_name)
        self.assertEqual(Employee.from_str("jane,doe,300").last_name, self.empl2.last_name)
        self.assertEqual(Employee.from_str("jane,doe,300").salary, self.empl2.salary)

        # add equality support optionlal


class TestDevOps(TestEmployee):
    def setUp(self):
        self.empl1 = DevOps("John", "Doe", 500,
                            ["Python", "Aws", "Bash", "Linux", "Laservision", "Bulletproof",
                             "Superspeed"])
        self.empl2 = DevOps("jane", "doe", 300)

    def tearDown(self):
        del self.empl1
        del self.empl2

    def test_add_skill(self):
        self.empl2.add_skill("Aws")
        self.assertEqual(self.empl2.skills, ["Aws"])
        self.empl2.add_skill("Python")
        self.assertEqual(self.empl2.skills, ["Aws", "Python"])

        self.empl1.add_skill("azure")
        self.empl1.add_skill("AZURE")
        self.empl1.add_skill("Azure")
        self.empl1.add_skill("azurE")
        self.assertIn("Azure", self.empl1.skills)
        self.assertNotIn("azurE", self.empl1.skills)
        self.assertNotIn("AZURE", self.empl1.skills)
        self.assertNotIn("azure", self.empl1.skills)

    def test_remove_skill(self):
        try:
            self.empl2.remove_skill("Aws")
        except KeyError:
            self.fail(msg="Key Error should be suppresed")

        self.empl1.remove_skill("Python")
        self.assertEqual(self.empl1.skills,
                         ["Aws", "Bash", "Linux", "Laservision", "Bulletproof", "Superspeed"])
        self.empl1.remove_skill("AWS")
        self.assertEqual(self.empl1.skills,
                         ["Bash", "Linux", "Laservision", "Bulletproof", "Superspeed"])


class TestManager(TestEmployee):
    @classmethod
    def setUpClass(cls):
        cls.empl1 = DevOps("John", "Doe", 500,
                           ["Python", "Aws", "Bash", "Linux", "Laservision", "Bulletproof",
                            "Superspeed"])
        cls.empl2 = DevOps("jane", "doe", 300)
        cls.empl3 = DevOps("James", "Holden", 300, ["Aws", "Azure"])
        cls.empl4 = DevOps("Amos", "Burton", 300, ["windows", "support"])
        cls.empl5 = DevOps("Alex", "Kamal", 300)
        cls.empl6 = DevOps("Naomi", "Nagata", 300)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.mng1 = Manager("jane", "doe", 600)
        self.mng2 = Manager("jane", "doe", 600, [self.empl1, self.empl2])

    def tearDown(self):
        del self.mng1
        del self.mng2

    def test_add_subordinate(self):
        self.mng1.add_subordinate(self.empl3)
        self.assertIn(self.empl3, self.mng1.subordinates)
        self.mng1.add_subordinate(self.empl4)
        self.assertIn(self.empl4, self.mng1.subordinates)

    def test_remove_subordinate(self):
        try:
            self.mng1.remove_subordinate(self.empl5)
        except KeyError:
            self.fail(msg="Key Error should be suppresed")

        # removal with object
        self.mng2.remove_subordinate(self.empl2)
        self.assertNotIn(self.empl2, self.mng2.subordinates)

        # remove by email
        self.mng2.remove_subordinate(self.empl1.email)
        self.assertEqual(self.mng2.subordinates, [])


if __name__ == "__main__":
    unittest.main()
