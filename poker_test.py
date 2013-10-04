import unittest
import poker

class Testpoker(unittest.TestCase):

    def test1_numhand(self):
        """test_numhand ["2C","3C","4D","5H","6S"]-->[2,4,4,5,6]"""
        actual = poker.numhand(["2C","3C","4D","5H","6S"])
        expected = ["2","3","4","5","6"]
        self.assertEqual(actual, expected)
    def test2_numhand(self):
        """test_numhand ["8D","9H","3D","3C","7S"]-->[8,9,3,3,7]"""
        actual = poker.numhand(["8D","9H","3D","3C","7S"])
        expected = ["8","9","3","3","7"]
        self.assertEqual(actual, expected)
    def test3_numhand(self):
        """test_numhand ["1D","1C","1H","6S","JD"]-->[1,1,1,6,J]"""
        actual = poker.numhand(["1D","1C","1H","6S","JD"])
        expected = ["1","1","1","6","J"]
        self.assertEqual(actual, expected)
    def test1_dokhand(self):
        """test_dokhand ["2C","3C","4D","5H","6S"]-->['C','C','D','H','S']"""
        actual = poker.dokhand(["2C","3C","4D","5H","6S"])
        expected = ['C','C','D','H','S']
        self.assertEqual(actual, expected)
    def test2_dokhand(self):
        """test_dokhand ["JC","TC","9C","8C","7C"]-->['C','C','C','C','C']"""
        actual = poker.dokhand(["JC","TC","9C","8C","7C"])
        expected = ['C','C','C','C','C']
        self.assertEqual(actual, expected)
    def test3_dokhand(self):
        """test_dokhand ["8D","9H","3D","3C","7S"]-->["D","H","D","C","S"]"""
        actual = poker.dokhand(["8D","9H","3D","3C","7S"])
        expected = ["D","H","D","C","S"]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
