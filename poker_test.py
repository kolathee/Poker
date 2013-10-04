import unittest
import poker

class TestNumhand(unittest.TestCase):

    def test1_numhand(self):
        """test_numhand ["2C","3C","4D","5H","6S"]-->[2,3,4,5,6]"""
        actual = poker.numhand(["2C","3C","4D","5H","6S"])
        expected = [2,3,4,5,6]
        self.assertEqual(actual, expected)
    def test2_numhand(self):
        """test_numhand ["8D","9H","3D","3C","7S"]-->[8,9,3,3,7]"""
        actual = poker.numhand(["8D","9H","3D","3C","7S"])
        expected = [8,9,3,3,7]
        self.assertEqual(actual, expected)
    def test3_numhand(self):
        """test_numhand ["2D","2C","2H","6S","JD"]-->[2,2,2,6,J]"""
        actual = poker.numhand(["2D","2C","2H","6S","JD"])
        expected = [2,2,2,6,11]
        self.assertEqual(actual, expected)

class TestDokhand(unittest.TestCase):

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

class TestFlush(unittest.TestCase):

    def test1_is_flush(self):
        """test_is_flush ['JC', 'TC', '9C', '8C', '7C']-->True"""
        actual = poker.is_flush(['JC', 'TC', '9C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test2_is_flush(self):
        """test_is_flush ['5S', '5H', '5D', '5C', 'KS']-->False"""
        actual = poker.is_flush(['5S', '5H', '5D', '5C', 'KS'])
        expected = False
        self.assertEqual(actual, expected)

class TestStraight(unittest.TestCase):        

    def test1_is_straight(self):
        """test1_is_straight ['6S', '8H', '7S', '9C', 'TS']-->True"""
        actual = poker.is_straight(['6S', '8H', '7S', '9C', 'TS'])
        expected = True
        self.assertEqual(actual, expected)
    def test2_is_straight(self):
        """test2_is_straight ['QC', '2S', '8S', '3S', '6S']-->False"""
        actual = poker.is_straight(['QC', '2S', '8S', '3S', '6S'])
        expected = False
        self.assertEqual(actual, expected)
    def test3_is_straight(self):
        """test3_is_straight ['TS', 'TH', 'JC', 'KH', '4H']-->False"""
        actual = poker.is_straight(['TS', 'TH', 'JC', 'KH', '4H'])
        expected = False
        self.assertEqual(actual, expected)
    def test4_is_straight(self):
        """test4_is_straight ['KH', 'QC', 'TC', 'JS', 'AC']-->True"""
        actual = poker.is_straight(['KH', 'QC', 'TC', 'JS', 'AC'])
        expected = True
        self.assertEqual(actual, expected)
    def test5_is_straight(self):
        """test5_is_straight ['JH', '6C', '3H', '2S', '6D']-->False"""
        actual = poker.is_straight(['JH', '6C', '3H', '2S', '6D'])
        expected = False
        self.assertEqual(actual, expected)

class TestRoyal(unittest.TestCase):

    def test1_is_royal(self):
        """test1_is_royal ['TC','JC','QC','KC','AC']-->True"""
        actual = poker.is_royal(['TC','JC','QC','KC','AC'])
        expected = True
        self.assertEqual(actual, expected)

    def test2_is_royal(self):
        """test2_is_royal ['TH','JH','QH','KH','AH']-->True"""
        actual = poker.is_royal(['TH','JH','QH','KH','AH'])
        expected = True
        self.assertEqual(actual, expected)

    def test3_is_royal(self):
        """test3_is_royal ['TH','JC','QH','KC','AH']-->False"""
        actual = poker.is_royal(['TH','JC','QH','KC','AH'])
        expected = False
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)