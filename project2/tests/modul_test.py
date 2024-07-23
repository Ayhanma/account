import unittest
from project2.modul1 import Data_Base

class Test_modul(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,3),5)

if __name__ == '__main__':
    unittest.main()