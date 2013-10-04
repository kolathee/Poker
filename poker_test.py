import unittest
import poker

class TestNumhand(unittest.TestCase):

    def test1_numhand(self):
        """test_numhand ['2C','3C','4D','5H','6S']-->[2,3,4,5,6]"""
        actual = poker.numhand(['2C','3C','4D','5H','6S'])
        expected = [2,3,4,5,6]
        self.assertEqual(actual, expected)
    def test2_numhand(self):
        """test_numhand ['8D','9H','3D','3C','7S']-->[8,9,3,3,7]"""
        actual = poker.numhand(["8D","9H","3D","3C","7S"])
        expected = [8,9,3,3,7]
        self.assertEqual(actual, expected)
    def test3_numhand(self):
        """test_numhand ['2D','2C','2H','6S','JD']-->[2,2,2,6,11]"""
        actual = poker.numhand(['2D','2C','2H','6S','JD'])
        expected = [2,2,2,6,11]
        self.assertEqual(actual, expected)

class TestDokhand(unittest.TestCase):

    def test1_dokhand(self):
        """test_dokhand ['2C','3C','4D','5H','6S']-->['C','C','D','H','S']"""
        actual = poker.dokhand(['2C','3C','4D','5H','6S'])
        expected = ['C','C','D','H','S']
        self.assertEqual(actual, expected)
    def test2_dokhand(self):
        """test_dokhand ['JC','TC','9C','8C','7C']-->['C','C','C','C','C']"""
        actual = poker.dokhand(['JC','TC','9C','8C','7C'])
        expected = ['C','C','C','C','C']
        self.assertEqual(actual, expected)
    def test3_dokhand(self):
        """test_dokhand ['8D','9H','3D','3C','7S']-->['D','H','D','C','S']"""
        actual = poker.dokhand(['8D','9H','3D','3C','7S'])
        expected = ['D','H','D','C','S']
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
    def test3_is_flush(self):
        """test_is_flush ['QD','9D','7D','4D','3D']-->True"""
        actual = poker.is_flush(['QD','9D','7D','4D','3D'])
        expected = True
        self.assertEqual(actual, expected)
    def test4_is_flush(self):
        """test_is_flush ['KH','QH','9H','5H','4H']-->True"""
        actual = poker.is_flush(['KH','QH','9H','5H','4H'])
        expected = True
        self.assertEqual(actual, expected)
    def test5_is_flush(self):
        """test_is_flush ['5S', '5H', '5D', '5C', 'KS']-->False"""
        actual = poker.is_flush(['5S', '5H', '5D', '5C', 'KS'])
        expected = False
        self.assertEqual(actual, expected)
    def test6_is_flush(self):
        """test_is_flush ['4H','4D','4S','4C','2D']-->False"""
        actual = poker.is_flush(['4H','4D','4S','4C','2D'])
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
        """test5_is_straight ['QC','JS','TS','9H','8H']-->True"""
        actual = poker.is_straight(['QC','JS','TS','9H','8H'])
        expected = True
        self.assertEqual(actual, expected)
    def test6_is_straight(self):
        """test6_is_straight ['AC','KC','QD','JS','TS']-->True"""
        actual = poker.is_straight(['AC','KC','QD','JS','TS'])
        expected = True
        self.assertEqual(actual, expected)
    def test7_is_straight(self):
        """test7_is_straight ['JH', '6C', '3H', '2S', '6D']-->False"""
        actual = poker.is_straight(['JH', '6C', '3H', '2S', '6D'])
        expected = False
        self.assertEqual(actual, expected)
    def test8_is_straight(self):
        """test8_is_straight ['3S','2D','AH','KS','QC']-->False"""
        actual = poker.is_straight(['3S','2D','AH','KS','QC'])
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

class Testthree_of_kind(unittest.TestCase):
    def test1_is_three_of_kind(self):
        """test1_is_Three_of_kind ['3C', 'TD', '5D', '4H', '8H']-->False"""
        actual = poker.is_three_of_kind(['3C', 'TD', '5D', '4H', '8H'])
        expected = False
        self.assertEqual(actual, expected)
    def test2_is_three_of_kind(self):
        """test2_is_Three_of_kind ['5S', '5D', '5C', '8C', '5H']-->False"""
        actual = poker.is_three_of_kind(['5S', '5D', '5C', '8C', '5H'])
        expected = False
        self.assertEqual(actual, expected)
    def test3_is_three_of_kind(self):
        """test3_is_Three_of_kind ['8C', 'KH', '8S', '9S', '6D']-->False"""
        actual = poker.is_three_of_kind(['8C', 'KH', '8S', '9S', '6D'])
        expected = False
        self.assertEqual(actual, expected)
    def test4_is_three_of_kind(self):
        """test4_is_Three_of_kind ['TC', 'TD', '9H', '6C', 'AS']-->False"""
        actual = poker.is_three_of_kind(['TC', 'TD', '9H', '6C', 'AS'])
        expected = False
        self.assertEqual(actual, expected)
    def test5_is_three_of_kind(self):
        """test5_is_Three_of_kind ['AS', 'AD', '3C', '8C', 'AH']-->True"""
        actual = poker.is_three_of_kind(['AS', 'AD', '3C', '8C', 'AH'])
        expected = True
        self.assertEqual(actual, expected)
    def test6_is_three_of_kind(self):
        """test6_is_Three_of_kind ['AS', 'AD', '3C', '8C', 'AH']-->True"""
        actual = poker.is_three_of_kind(['AS', 'AD', '3C', '8C', 'AH'])
        expected = True
        self.assertEqual(actual, expected)

class Testfour_of_kind(unittest.TestCase):
    def test1_is_four_of_kind(self):
        """test1_is_Three_of_kind ['9C','9S','9D','9H','JH']-->True"""
        actual = poker.is_four_of_kind(['9C','9S','9D','9H','JH'])
        expected = True
        self.assertEqual(actual, expected)
    def test2_is_four_of_kind(self):
        """test2_is_Three_of_kind ['7D','7H','7S','7C','TC']-->True"""
        actual = poker.is_four_of_kind(['7D','7H','7S','7C','TC'])
        expected = True
        self.assertEqual(actual, expected)
    def test3_is_four_of_kind(self):
        """test3_is_Three_of_kind ['8C', 'KH', '8S', '9S', '6D']-->False"""
        actual = poker.is_four_of_kind(['8C', 'KH', '8S', '9S', '6D'])
        expected = False
        self.assertEqual(actual, expected)
    def test4_is_four_of_kind(self):
        """test4_is_Three_of_kind ['QS', '6D', '5S', '6S', '6C']-->False"""
        actual = poker.is_four_of_kind(['QS', '6D', '5S', '6S', '6C'])
        expected = False
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
