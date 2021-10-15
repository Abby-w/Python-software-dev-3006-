#questions:

#does each function only get the arguments shown in the instructions
#how to call the score function in init
#does add card perform like get_card
#should init call add card if it is not given a list
#canonical representation of the string?

import random
from collections import namedtuple
from collections import defaultdict
import sys
import csv
Stand = namedtuple('Stand', ['stand', 'total'])
Score = namedtuple('Score', ['total', 'soft_ace_count'])



class Hand:

    def __init__(self, cards=None):
        self.cards=cards
        if cards== None:
            self.cards=[]
            self.total=0
            self.stand_on_soft=0
        else:
            total,soft_ace_count = self.score()
            self.total=total
            self.soft_ace_count=soft_ace_count

    def __str__(self):
        dict_cards={1:"ace", 2:"two",3:"three", 4: "four", 5: "five", 6:"six",
        7:"seven", 8: "eight", 9: "nine", 10: "ten", 11:"jack", 12:"queen",
        13: "king"}
        string=''
        for card in self.cards:
            string+= dict_cards.get(card)
        return string


    def add_card(self):
        self.cards+=[random.randint(1,13)]


    def is_blackjack(self):
        if self.total==21 and self.soft_ace_count==1:
            return True

    def is_bust(self):
        if self.total>=21:
            return True

    def score(self):
        """Counts the total value of the cards in the hand and the number of soft
        aces
        Parameters:
            cards: A list of the cards in a single blackjack hand

        Returns:
            S= namedtuple of the card total and the soft ace coount
        """

        self.soft_ace_count=0

        #change the jack, queen and king cards to a value of 10
        for index,value in enumerate(self.cards):
            if value >10:
                self.cards[index]=10
        #calculate the total value
        self.total=sum(cards)
        #account for possible soft aces in the hand
        if (self.total<=11) and (1 in self.cards):
            self.total=self.total + 10
            self.soft_ace_count=1
        #add information to the named tuple
        S= Score(total,soft_ace_count)
        return S



class Strategy:


    def __init__(self, stand_on_value, stand_on_soft):
        self.stand_on_value=stand_on_value
        self.stand_on_soft=stand_on_soft

    def __repr__(self):
        #this is not correct
        return string

    def __str__(self):
        if stand_on_soft==True:
            strategy='S'
        else:
            strategy='H'
        strategy+=str(stand_on_value)

    def stand(self, hand):
        #needs to be corrected

        """Determines if the player should stand or hit based on their current hand
        Parameters:
            stand_on_value: the integer to determine if they should stand
            stand_on_soft: A boolean representing stand on soft or stand on hard
            cards: A list of the cards in a single blackjack hand

        Returns:
            S= namedtuple of boolean whether to stand or not and the total value of
            the cards
        """



        #case one: total is less than the stand on value -- always hit
        if hand.total < self.stand_on_value:
            stand = False
        #case two: total is equal than the stand on value
        if hand.total== self.stand_on_value:
            if self.stand_on_soft==True:
                #stand
                stand= True
            if self.stand_on_soft==False:
                if hand.soft_ace_count==0:
                    #stand
                    stand = True
                if hand.soft_ace_count==1:
                    #hit
                    stand =  False
        #case three: total is greater than the stand on value  --always stand
        if hand.total > self.stand_on_value:
            stand = True
        #add information to the named tuple
        S= Stand(stand,hand.total)
        return S

    def play(self):
        """runs a single hand to completion
        Parameters:
            stand_on_value: Integer between 13 and 21
            stand_on_soft: Boolean, whether to stand on soft or stand on hard
        Returns:
            total:The total value of cards at the end of a hand
        """
        hand = Hand()
        run="yes"
        #check the total and determine whether to hit or stand
        while run=="yes":

            stay=self.stand(hand)[0]
            #determine if hand is bust
            if stay==True:
                run="no"
            #get another card and re-run stand function
            else:
                Hand.add_card(hand)
        #Only return 22 if bust
        if hand.total >22:
            hand.total=22
        return total

test=Strategy(17,True)
print(test.play())



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



    def Test1(self):
        """
        Docstrings are printed in most test runners.
        """
        test = "9+4"
        expect = ["9", "+", "4"]
        failure_msg = 'lexer({0}) should return {1} but returned {2}'
        actual = lexer(test)
        self.assertListEqual(expect, actual, failure_msg.format(test, expect, actual))
