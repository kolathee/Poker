import unittest
import poker_test

class Testpoker(unittest.TestCase):

    def test1_numhand(self):
        """test_numhand ["2C","3C","4D","5H","6S"]-->[2,4,4,5,6]"""
        actual = poker_test.numhand(["2C","3C","4D","5H","6S"])
        expected = [2,3,4,5,6]
        self.assertEqual(actual, expected)
    def test1_dokhand(self):
        """test_dokhand ["2C","3C","4D","5H","6S"]-->['C','D','H','S']"""
        actual = poker_test.dokhand(["2C","3C","4D","5H","6S"])
        expected = ['C','D','H','S']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
