#run with "python3 -m unittest test_blackjack2.py"

#import packages
import unittest
from blackjack3 import Hand
from blackjack3 import Strategy
class TestScore(unittest.TestCase):
    """Tests the function score with 7 test cases
    Parameters
    ----------
    unittest.TestCase: base individual testing unit from the unit test

    Returns
    -------
    testing results
    """


    def test_str(self):
        cards=Hand([1,2,3,4,5,6,7,8,9,10,11,12,13])
        ret = cards.__str__()
        self.assertEqual(ret, 'Hand: cards=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])')


    def test_is_blackjack_false(self):
        cards=Hand([2,2])
        ret = cards.is_blackjack()
        self.assertEqual(ret, False)

    def test_is_blackjack_true(self):
        cards=Hand([1,10])
        ret = cards.is_blackjack()
        self.assertEqual(ret, True )


    def test_is_bust_false(self):
        cards=Hand([2,2])
        ret = cards.is_bust()
        self.assertEqual(ret, False)

    def test_is_bust_true(self):
        cards=Hand([9,8,10])
        ret = cards.is_bust()
        self.assertEqual(ret, True )

#test with 5,5, and 10
    def test_one(self):
        cards=Hand([3,12])
        ret = cards.score()
        self.assertEqual(ret, (13,0))
#test with 5,5, and 10
    def test_two(self):
        cards=Hand([5,5,10])
        ret = cards.score()
        self.assertEqual(ret, (20,0))
#test with 11,10 and 1
    def test_three(self):
        cards=Hand([11,10,1])
        ret = cards.score()
        self.assertEqual(ret, (21,0))
#test with 1 and 5
    def test_four(self):
        cards=Hand([1,5])
        ret = cards.score()
        self.assertEqual(ret, (16,1))
#test with 1,1, and 5
    def test_five(self):
        cards=Hand([1,1,5])
        ret = cards.score()
        self.assertEqual(ret, (17,1))
#test with 1,1,1, and 7
    def test_six(self):
        cards=Hand([1,1,1,7])
        ret = cards.score()
        self.assertEqual(ret, (20,1))
#test with 7,8, and 10
    def test_seven(self):
        cards=Hand([7,8,10])
        ret = cards.score()
        self.assertEqual(ret, (25,0))


    def test_repr(self):
        strat=Strategy(17, True)
        ret = strat.__repr__()
        self.assertEqual(ret, "Strategy(17, True)")



    def test_str_soft(self):
        strat=Strategy(17, True)
        ret = strat.__str__()
        self.assertEqual(ret, "S17")

    def test_str_hard(self):
        strat=Strategy(10, False)
        ret = strat.__str__()
        self.assertEqual(ret, "H10")



        #less than stand on value
    def test_True_less(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([3,10]))
        self.assertEqual(ret, (False, 13))

    def test_True_less_ace(self):
        strat=Strategy(17, True)
        ret = strat.stand(Hand([1,1]))
        self.assertEqual(ret, (False, 12))

    def test_False_less(self):
        strat=Strategy(17, False)
        ret = strat.stand(Hand([3,10]))
        self.assertEqual(ret, (False,13))

    def test_False_less_ace(self):
        strat=Strategy(17, False)
        ret = strat.stand(Hand([1,1]))
        self.assertEqual(ret, (False, 12))

#equal to stand on value, no aces

    def test_True_equal(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([7,10]))
        self.assertEqual(ret, (True, 17))

    def test_False_equal(self):
        strat =Strategy(17, False)
        ret = strat.stand(Hand([7,10]))
        self.assertEqual(ret, (True, 17))

#equal to stand on value, soft ace
    def test_True_equal_soft_ace(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([1,6]))
        self.assertEqual(ret, (True, 17))

    def test_False_equal_soft_ace(self):
        strat =Strategy(17, False)
        ret = strat.stand(Hand([1,6]))
        self.assertEqual(ret, (False, 17))

#equal to stand on value, hard ace
    def test_True_equal_hard_ace(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([1,6,10]))
        self.assertEqual(ret, (True, 17))

    def test_False_equal_hard_ace(self):
        strat =Strategy(17, False)
        ret = strat.stand(Hand([1,6,10]))
        self.assertEqual(ret, (True, 17))



#greater than stand on value
    def test_True_greater(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([9,10]))
        self.assertEqual(ret, (True, 19))

    def test_True_greater_hard_ace(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([1,8,10]))
        self.assertEqual(ret, (True, 19))

    def test_True_greater_soft_ace(self):
        strat =Strategy(17, True)
        ret = strat.stand(Hand([1,8]))
        self.assertEqual(ret, (True, 19))

    def test_False_greater(self):
        strat =Strategy(17, False)
        ret = strat.stand(Hand([9,10]))
        self.assertEqual(ret, (True, 19))

    def test_False_greater__hard_ace(self):
        strat =Strategy(17, False)
        ret = strat.stand(Hand([1,8,10]))
        self.assertEqual(ret, (True, 19))

    def test_True_greater_soft_ace(self):
        strat =Strategy(17, False)
        ret = strat.stand(Hand([1,8]))
        self.assertEqual(ret, (True, 19))


    #print statements to check that setup and teardown were completed
    def setUp(self):
        print("setUp runs before each test case.")

    def tearDown(self):
        print("teardown runs after each test case.")

if __name__ == '__main__':
    unittest.main()
