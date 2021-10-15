#run with "python3 -m unittest test_blackjack2.py"

#import packages
import unittest
from blackjack2 import score

class TestScore(unittest.TestCase):
    """Tests the function score with 7 test cases
    Parameters
    ----------
    unittest.TestCase: base individual testing unit from the unit test

    Returns
    -------
    testing results
    """

    print("Test of Score function")
#test with 3 and 12
    def test_one(self):
        ret = score([3,12])
        self.assertEqual(ret, (13,0))
#test with 5,5, and 10
    def test_two(self):
        ret = score([5,5,10])
        self.assertEqual(ret, (20,0))
#test with 11,10 and 1
    def test_three(self):
        ret = score([11,10,1])
        self.assertEqual(ret, (21,0))
#test with 1 and 5
    def test_four(self):
        ret = score([1,5])
        self.assertEqual(ret, (16,1))
#test with 1,1, and 5
    def test_five(self):
        ret = score([1,1,5])
        self.assertEqual(ret, (17,1))
#test with 1,1,1, and 7
    def test_six(self):
        ret = score([1,1,1,7])
        self.assertEqual(ret, (20,1))
#test with 7,8, and 10
    def test_seven(self):
        ret = score([7,8,10])
        self.assertEqual(ret, (25,0))
#print statements to check that setup and teardown were completed
    def setUp(self):
        print("setUp runs before each test case.")

    def tearDown(self):
        print("teardown runs after each test case.")

from blackjack2 import stand

class TestStand(unittest.TestCase):
    """Tests the function score with ? test cases
    Parameters
    ----------
    unittest.TestCase: base individual testing unit from the unit test

    Returns
    -------
    testing results
    """
    print("Test of Stand function")
#less than stand on value
    def test_True_less(self):
        ret = stand(17, True, [3,10])
        self.assertEqual(ret, (False, 13))

    def test_True_less_ace(self):
        ret = stand(17, True, [1,1])
        self.assertEqual(ret, (False, 12))

    def test_False_less(self):
        ret = stand(17, False, [3,10])
        self.assertEqual(ret, (False,13))

    def test_False_less_ace(self):
        ret = stand(17, False, [1,1])
        self.assertEqual(ret, (False, 12))

#equal to stand on value, no aces

    def test_True_equal(self):
        ret = stand(17, True, [7,10])
        self.assertEqual(ret, (True, 17))

    def test_False_equal(self):
        ret = stand(17, False, [7,10])
        self.assertEqual(ret, (True, 17))

#equal to stand on value, soft ace
    def test_True_equal_soft_ace(self):
        ret = stand(17, True, [1,6])
        self.assertEqual(ret, (True, 17))

    def test_False_equal_soft_ace(self):
        ret = stand(17, False, [1,6])
        self.assertEqual(ret, (False, 17))

#equal to stand on value, hard ace
    def test_True_equal_hard_ace(self):
        ret = stand(17, True, [1,10,6])
        self.assertEqual(ret, (True, 17))

    def test_False_equal_hard_ace(self):
        ret = stand(17, False, [1,10,6])
        self.assertEqual(ret, (True, 17))



#greater than stand on value
    def test_True_greater(self):
        ret = stand(17, True, [9,10])
        self.assertEqual(ret, (True, 19))

    def test_True_greater_hard_ace(self):
        ret = stand(17, True, [1,10,8])
        self.assertEqual(ret, (True, 19))

    def test_True_greater_soft_ace(self):
        ret = stand(17, True, [1,8])
        self.assertEqual(ret, (True, 19))

    def test_False_greater(self):
        ret = stand(17, False, [9,10])
        self.assertEqual(ret, (True, 19))

    def test_False_greater__hard_ace(self):
        ret = stand(17, False, [1,10,8])
        self.assertEqual(ret, (True, 19))

    def test_True_greater_soft_ace(self):
        ret = stand(17, False, [1,8])
        self.assertEqual(ret, (True, 19))

    #print statements to check that setup and teardown were completed
        def setUp(self):
            print("setUp runs before each test case.")

        def tearDown(self):
            print("teardown runs after each test case.")

if __name__ == '__main__':
    unittest.main()
