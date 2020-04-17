import json
import unittest
from unittest import TestCase
from unittest.mock import patch

import os
import sys

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from python.module7.top250 import parse_top_250


class TestParseTop250(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_data = open(os.path.join(SCRIPT_DIR, 'mockImdb.html'), encoding="UTF-8")

    @classmethod
    def tearDownClass(cls):
        cls.mock_data.close()

    def test_parse_top_250(self):
        link = "https://imdb.com/chart/top"
        # res = requests.get(link, headers={"Accept-Language": "En-us"})
        with patch('python.module7.top250.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = self.mock_data

            parse_top_250(os.path.join(SCRIPT_DIR, "top250.json"))
            mocked_get.assert_called_with(link, headers={'Accept-Language': 'En-us'})

            with open(os.path.join(SCRIPT_DIR, "top250.json")) as result_json:
                result_data: list = json.load(result_json)
                print(result_data)
                self.assertEqual(list(filter(lambda x: x.get("The Shawshank Redemption") is not None, result_data))[0],
                                 {"The Shawshank Redemption": {"Position": "1", "Year": "1994", "Director": "Frank Darabont",
                                  "Crew": "Tim Robbins, Morgan Freeman", "Rating": "9.2"}})

                self.assertEqual(list(filter(lambda x: x.get("The Godfather") is not None, result_data))[0],
                                 {"The Godfather": {"Position": "2", "Year": "1972", "Director": "Francis Ford Coppola",
                                  "Crew": "Marlon Brando, Al Pacino", "Rating": "9.2"}})

                self.assertEqual(list(filter(lambda x: x.get("Goodfellas") is not None, result_data))[0],
                                 {"Goodfellas":{"Position": "17", "Year": "1990", "Director": "Martin Scorsese",
                                  "Crew": "Robert De Niro, Ray Liotta", "Rating": "8.7"}})


if __name__ == "__main__":
    unittest.main()
