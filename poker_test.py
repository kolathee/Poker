import unittest
import poker

class TestNumhand(unittest.TestCase):

    def test1_numhand(self):
        """test_numhand ['2C','3C','4D','5H','6S']-->[2,3,4,5,6]"""
        actual = poker.numhand(['2C','3C','4D','5H','6S'])
        expected = [6,5,4,3,2]
        self.assertEqual(actual, expected)
    def test2_numhand(self):
        """test_numhand ['8D','9H','3D','3C','7S']-->[8,9,3,3,7]"""
        actual = poker.numhand(["8D","9H","3D","3C","7S"])
        expected = [9,8,7,3,3]
        self.assertEqual(actual, expected)
    def test3_numhand(self):
        """test_numhand ['2D','2C','2H','6S','JD']-->[2,2,2,6,11]"""
        actual = poker.numhand(['2D','2C','2H','6S','JD'])
        expected = [11,6,2,2,2]
        self.assertEqual(actual, expected)

class TestDokhand(unittest.TestCase):

    def test1_dokhand(self):
        """test_dokhand ['2C','3C','4D','5H','6S']-->['C','C','D','H','S']"""
        actual = poker.dokhand(['2C','3C','4D','5H','6S'])
        expected = [0.1,0.1,0.2,0.3,0.4]
        self.assertEqual(actual, expected)
    def test2_dokhand(self):
        """test_dokhand ['JC','TC','9C','8C','7C']-->['C','C','C','C','C']"""
        actual = poker.dokhand(['JC','TC','9C','8C','7C'])
        expected = [0.1,0.1,0.1,0.1,0.1]
        self.assertEqual(actual, expected)
    def test3_dokhand(self):
        """test_dokhand ['8D','9H','3D','3C','7S']-->['D','H','D','C','S']"""
        actual = poker.dokhand(['8D','9H','3D','3C','7S'])
        expected = [0.2,0.3,0.2,0.1,0.4]
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
        """test6_is_Three_of_kind ['2C', '7D', '6H', '2H', '2S']-->True"""
        actual = poker.is_three_of_kind(['2C', '7D', '6H', '2H', '2S'])
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

class TestTwo_pair(unittest.TestCase):
    def test1_is_two_pair(self):
        """test1_is_two_pair ['2D', '9D', '2S', 'AD', 'AH']-->True"""
        actual = poker.is_two_pair(['2D', '9D', '2S', 'AD', 'AH'])
        expected = True
        self.assertEqual(actual, expected)
    def test2_is_two_pair(self):
        """test2_is_two_pair ['8S', '7S', '2S', '8D', '7C']-->True"""
        actual = poker.is_two_pair(['8S', '7S', '2S', '8D', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test3_is_two_pair(self):
        """test3_is_two_pair ['3C', '4H', '5D', 'TC', 'AC']-->False"""
        actual = poker.is_two_pair(['3C', '4H', '5D', 'TC', 'AC'])
        expected = False
        self.assertEqual(actual, expected)
    def test4_is_two_pair(self):
        """test4_is_two_pair ['9H', 'AS', '5C', '5C', 'JC']-->False"""
        actual = poker.is_two_pair(['9H', 'AS', '5C', '5C', 'JC'])
        expected = False
        self.assertEqual(actual, expected)

class TestOne_pair(unittest.TestCase):
    def test1_is_one_pair(self):
        """test1_is_one_pair ['6D', '4C', 'AH', 'JC', 'AD']-->True"""
        actual = poker.is_one_pair(['6D', '4C', 'AH', 'JC', 'AD'])
        expected = True
        self.assertEqual(actual, expected)
    def test2_is_one_pair(self):
        """test2_is_one_pair ['QH', 'AH', 'QC', '4S', '8S']-->True"""
        actual = poker.is_one_pair(['QH', 'AH', 'QC', '4S', '8S'])
        expected = True
        self.assertEqual(actual, expected)
    def test3_is_one_pair(self):
        """test3_is_one_pair ['KS', 'QD', '5S', 'TH', '6C']-->False"""
        actual = poker.is_one_pair(['KS', 'QD', '5S', 'TH', '6C'])
        expected = False
        self.assertEqual(actual, expected)
    def test4_is_one_pair(self):
        """test4_is_one_pair ['4D', '5C', 'JS', 'QH', '3H']-->False"""
        actual = poker.is_one_pair(['4D', '5C', 'JS', 'QH', '3H'])
        expected = False
        self.assertEqual(actual, expected)
    def test5_is_one_pair(self):
        """test1_is_one_pair ['2D', '9D', '2S', 'AD', 'AH']-->False"""
        actual = poker.is_one_pair(['2D', '9D', '2S', 'AD', 'AH'])
        expected = False
        self.assertEqual(actual, expected)

class TestFullHouse(unittest.TestCase):
    def test1_is_fullhouse(self):
        """test1_is_fullhouse ['4D', '4S', '2D', '4D', '2H']-->True"""
        actual = poker.is_fullhouse(['4D', '4S', '2D', '4D', '2H'])
        expected = True
        self.assertEqual(actual, expected)
    def test2_is_fullhouse(self):
        """test2_is_fullhouse ['JD', '5C', '7D', '3D', '2D']-->False"""
        actual = poker.is_fullhouse(['JD', '5C', '7D', '3D', '2D'])
        expected = False
        self.assertEqual(actual, expected)
    def test3_is_fullhouse(self):
        """test3_is_fullhouse ['5D', 'TS', '5C', 'TD', '5H']-->True"""
        actual = poker.is_fullhouse(['5D', 'TS', '5C', 'TD', '5H'])
        expected = True
        self.assertEqual(actual, expected)
    def test4_is_fullhouse(self):
        """test4_is_fullhouse ['4D', '5C', 'JS', 'QH', '3H']-->False"""
        actual = poker.is_fullhouse(['4D', '5C', 'JS', 'QH', '3H'])
        expected = False
        self.assertEqual(actual, expected)

class HandRank(unittest.TestCase):
    def test1_handrank(self):
        """test1_handrank ['TH','JH','QH','KH','AH']-->10"""
        actual = poker.handrank(['TH','JH','QH','KH','AH'])
        expected = (10,0)
        self.assertEqual(actual, expected)
    def test2_handrank(self):
        """test2_handrank ['TC','JC','QC','KC','AC']-->10"""
        actual = poker.handrank(['TC','JC','QC','KC','AC'])
        expected = (10,0)
        self.assertEqual(actual, expected)
    ##Royal
    def test3_handrank(self):
        """test3_handrank ['6S', '8S', '7S', '9S', 'TS']-->(9,10)"""
        actual = poker.handrank(['6S', '8S', '7S', '9S', 'TS'])
        expected = (9,10)
        self.assertEqual(actual, expected)
    def test4_handrank(self):
        """test4_handrank ['KC','QC','JC','TC','9C']-->(9,13)"""
        actual = poker.handrank(['KC','QC','JC','TC','9C'])
        expected = (9,13)
    ##straight Flush
        self.assertEqual(actual, expected)
    def test5_handrank(self):
        """test5_handrank ['9C','9S','9D','9H','JH']-->(8,9)"""
        actual = poker.handrank(['9C','9S','9D','9H','JH'])
        expected = (8,9)
        self.assertEqual(actual, expected)
    def test6_handrank(self):
        """test6_handrank ['8C','8S','8D','8H','JH']-->(8,8)"""
        actual = poker.handrank(['8C','8S','8D','8H','JH'])
        expected = (8,8)
        self.assertEqual(actual, expected)
    ##Four of a kind 
    def test7_handrank(self):
        """test7_handrank ['4D', '4S', '2D', '4D', '2H']-->(7,4,2)"""
        actual = poker.handrank(['4D', '4S', '2D', '4D', '2H'])
        expected = (7,4,2)
        self.assertEqual(actual, expected)
    def test8_handrank(self):
        """test8_handrank ['5D', 'TS', '5C', 'TD', '5H']-->(7,5,10)"""
        actual = poker.handrank(['5D', 'TS', '5C', 'TD', '5H'])
        expected = (7,5,10)
        self.assertEqual(actual, expected)
    ##Fullhouse
    def test9_handrank(self):
        """test9_handrank ['QD','9D','7D','4D','3D']-->(6,12)"""
        actual = poker.handrank(['QD','9D','7D','4D','3D'])
        expected = (6,12)
        self.assertEqual(actual, expected)
    def test10_handrank(self):
        """test10_handrank ['KH','QH','9H','5H','4H']-->(6,13)"""
        actual = poker.handrank(['KH','QH','9H','5H','4H'])
        expected = (6,13)
        self.assertEqual(actual, expected)
    ##Flush
    def test11_handrank(self):
        """test11_handrank ['6S', '8H', '7S', '9C', 'TS']-->(5,10)"""
        actual = poker.handrank(['6S', '8H', '7S', '9C', 'TS'])
        expected = (5,10)
        self.assertEqual(actual, expected)
    def test12_handrank(self):
        """test12_handrank ['QC','JS','TS','9H','8H']-->(5,12)"""
        actual = poker.handrank(['QC','JS','TS','9H','8H'])
        expected = (5,12)
        self.assertEqual(actual, expected)
    ##Straight
    def test13_handrank(self):
        """test13_handrank ['AS', 'AD', '3C', '8C', 'AH']-->(4,14,8,3)"""
        actual = poker.handrank(['AS', 'AD', '3C', '8C', 'AH'])
        expected = (4,14,8,3)
        self.assertEqual(actual, expected)
    def test14_handrank(self):
        """test14_handrank ['5C', '5D', '5S', '6S', '7C']-->(4,5,7,6)"""
        actual = poker.handrank(['5C', '5D', '5S', '6S', '7C'])
        expected = (4,5,7,6)
        self.assertEqual(actual, expected)
    ##Three of a kind 
    def test15_handrank(self):
        """test15_handrank ['2D', '9D', '2S', 'AD', 'AH']-->(3,14,2,9)"""
        actual = poker.handrank(['2D', '9D', '2S', 'AD', 'AH'])
        expected = (3,14,2,9)
        self.assertEqual(actual, expected)
    def test16_handrank(self):
        """test16_handrank ['3C', '4H', '3D', '4C', 'AC']-->(3,4,3,14)"""
        actual = poker.handrank(['3C', '4H', '3D', '4C', 'AC'])
        expected = (3,4,3,14)
        self.assertEqual(actual, expected)
    ##Two pair
    def test17_handrank(self):
        """test17_handrank ['6D', '4C', 'AH', 'JC', 'AD']-->(2,14,11,6,4)"""
        actual = poker.handrank(['6D', '4C', 'AH', 'JC', 'AD'])
        expected = (2,14,11,6,4)
        self.assertEqual(actual, expected)
    def test18_handrank(self):
        """test18_handrank ['QH', 'AH', 'QC', '4S', '8S']-->(2,12,14,8,4)"""
        actual = poker.handrank(['QH', 'AH', 'QC', '4S', '8S'])
        expected = (2,12,14,8,4)
        self.assertEqual(actual, expected)
    ##One pair
    def test19_handrank(self):
        """test19_handrank ['AS', '3H', '8D', '5H', 'KH']-->(1,14,13)"""
        actual = poker.handrank(['AS', '3H', '8D', '5H', 'KH'])
        expected = (1,14,13)
        self.assertEqual(actual, expected)
    def test20_handrank(self):
        """test20_handrank ['JC', '5D', 'KS', 'TH', '2H']-->(1,13,11)"""
        actual = poker.handrank(['JC', '5D', 'KS', 'TH', '2H'])
        expected = (1,13,11)
        self.assertEqual(actual, expected)
    ##High card
    
class WhoWin(unittest.TestCase):
    def test1_whowin(self):
        """test1_whowin [['QD','9D','7D','4D','3D'],['AS', '3H', '8D', '5H', 'KH'],['AS', '3H', '8D', '5H', 'KH']]-->['QD','9D','7D','4D','3D']"""
        actual = poker.whowin([['QD','9D','7D','4D','3D'],['AS', '3H', '8D', '5H', 'KH'],['AS', '3H', '8D', '5H', 'KH']])
        expected = [['QD','9D','7D','4D','3D']]
        self.assertEqual(actual, expected)
    def test2_whowin(self):
        """test2_whowin [['TC','JC','QC','KC','AC'],['TH','JH','QH','KH','AH'],['KC','QC','JC','TC','9C']]-->[['TC','JC','QC','KC','AC'],['TH','JH','QH','KH','AH']]"""
        actual = poker.whowin([['TC','JC','QC','KC','AC'],['TH','JH','QH','KH','AH'],['KC','QC','JC','TC','9C']])
        expected = [['TC','JC','QC','KC','AC'],['TH','JH','QH','KH','AH']]
        self.assertEqual(actual, expected)
    def test3_whowin(self):
        """test3_whowin [['6S', '8H', '7S', '9C', 'TS'],['8H','7D','6S','5C','4D'],['5D', '4S', '3D', '2D', '6H']]-->[['6S', '8H', '7S', '9C', 'TS']]"""
        actual = poker.whowin([['6S', '8H', '7S', '9C', 'TS'],['8H','7D','6S','5C','4D'],['5D', '4S', '3D', '2D', '6H']])
        expected = [['6S', '8H', '7S', '9C', 'TS']]
        self.assertEqual(actual, expected)
    def test4_whowin(self):
        """test4_whowin [['8C','8S','8D','8H','JH'],['9C','9S','9D','9H','JH'],['AS', 'AD', '3C', '8C', 'AH']]-->[['9C','9S','9D','9H','JH']]"""
        actual = poker.whowin([['8C','8S','8D','8H','JH'],['9C','9S','9D','9H','JH'],['AS', 'AD', '3C', '8C', 'AH']])
        expected = [['9C','9S','9D','9H','JH']]
        self.assertEqual(actual, expected)
    def test5_whowin(self):
        """test5_whowin [['AS', 'AD', '3C', '8C', 'AH'],['3C', '4H', '3D', '4C', 'AC'],['5D', 'TS', '5C', 'TD', '5H']]-->[['5D', 'TS', '5C', 'TD', '5H']]"""
        actual = poker.whowin([['AS', 'AD', '3C', '8C', 'AH'],['3C', '4H', '3D', '4C', 'AC'],['5D', 'TS', '5C', 'TD', '5H']])
        expected = [['5D', 'TS', '5C', 'TD', '5H']]
        self.assertEqual(actual, expected)
    
    def test6_whowin(self):
        """test6_whowin [['3D', '3C', 'TD', '8D', '9H'],['3H', '3S', 'AC', '6D', '2D'],['3S', '3H', '6C', '7D', '7H']]-->[['3S', '3H', '6C', '7D', '7H']]"""
        actual = poker.whowin([['3D', '3C', 'TD', '8D', '9H'],['3H', '3S', 'AC', '6D', '2D'],['3S', '3H', '6C', '7D', '7H']])
        expected = [['3S', '3H', '6C', '7D', '7H']]
        self.assertEqual(actual, expected)
    def test7_whowin(self):
        """test7_whowin [['JC', '5D', 'KS', 'TH', '2H'],['AS', '3H', '8D', '5H', 'KH']]-->[['AS', '3H', '8D', '5H', 'KH']]"""
        actual = poker.whowin([['JC', '5D', 'KS', 'TH', '2H'],['AS', '3H', '8D', '5H', 'KH']])
        expected = [['AS', '3H', '8D', '5H', 'KH']]
        self.assertEqual(actual, expected)
    def test8_whowin(self):
        """test8_whowin [['6D', '4C', 'AH', 'JC', 'AD'],['3C', '8H', '5D', '8C', '4C'],['3C', '4H', '3D', '4C', 'AC']]--> [['3C', '4H', '3D', '4C', 'AC']]"""
        actual = poker.whowin([['6D', '4C', 'AH', 'JC', 'AD'],['3C', '8H', '5D', '8C', '4C'],['3C', '4H', '3D', '4C', 'AC']])
        expected =  [['3C', '4H', '3D', '4C', 'AC']]
        self.assertEqual(actual, expected)
    def test9_whowin(self):
        """test9_whowin [['TC','JC','QC','KC','AC']]--> [['TC','JC','QC','KC','AC']]"""
        actual = poker.whowin([['TC','JC','QC','KC','AC']])
        expected =  [['TC','JC','QC','KC','AC']]
        self.assertEqual(actual, expected)
    
    def test10_whowin(self):
        """test10_whowin [['TC', '4C', '5H', '8S', '6D'],['6S', '3H', 'AD', '9C', '9S']]--> [['6S', '3H', 'AD', '9C', '9S']]"""
        actual = poker.whowin([['TC', '4C', '5H', '8S', '6D'],['6S', '3H', 'AD', '9C', '9S']])
        expected =  [['6S', '3H', 'AD', '9C', '9S']]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
