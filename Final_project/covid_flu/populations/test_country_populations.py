"""Unit tests for the flu data program."""
import unittest

from country_populations import *

class Test_Population_Stats(unittest.TestCase):
    def test_iterable(self):
        iter(Population_Stats())
if __name__ == '__main__':
    unittest.main()
