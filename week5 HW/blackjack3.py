import random
from collections import namedtuple
import sys
import csv
Stand = namedtuple('Stand', ['stand', 'total'])
Score = namedtuple('Score', ['total', 'soft_ace_count'])



class Hand:

    def __init__(self, cards=None):
        #initiate cards, total and soft ace count
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
        #string representation of hand
        return f'Hand: cards={self.cards})'

    def add_card(self):
        #add card to hand and call score
        self.cards+=[random.randint(1,13)]
        total,soft_ace_count = self.score()

    def is_blackjack(self):
        #check if hand is blackjack
        if self.total==21 and self.soft_ace_count==1:
            return True
        else:
            return False

    def is_bust(self):
        #check if hand is bust
        if self.total>21:
            return True
        else:
            return False

    def score(self):
        """Counts the total value of the cards in the hand and the number of soft
        aces
        """
        #set variables
        self.total=0
        self.soft_ace_count=0

        #change the jack, queen and king cards to a value of 10
        for index,value in enumerate(self.cards):
            if value >10:
                self.cards[index]=10
        #calculate the total value
        self.total=sum(self.cards)
        #account for possible soft aces in the hand
        if (self.total<=11) and (1 in self.cards):
            self.total=self.total + 10
            self.soft_ace_count=1
        #add information to the named tuple
        S= Score(self.total,self.soft_ace_count)
        return S


class Strategy:

    def __init__(self, stand_on_value, stand_on_soft):
        #initiate stand on soft and stand on value
        self.stand_on_value=stand_on_value
        self.stand_on_soft=stand_on_soft

    def __repr__(self):
        #canonical string representation
        return f'Strategy({self.stand_on_value}, {self.stand_on_soft})'

    def __str__(self):
        #shorthand string representation
        strategy=''
        if self.stand_on_soft==True:
            sos='S'
        else:
            sos='H'
        strategy+=sos + str(self.stand_on_value)
        return strategy

    def stand(self, hand):
        """Determines if the player should stand or hit based on their current hand

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
        S=Stand(stand,hand.total)
        return S


    def play(self):
        """runs a single hand to completion

        """
        #inititalize hand
        hand = Hand()
        hand.add_card()
        hand.add_card()
        run="yes"
        #check the total and determine whether to hit or stand
        while run=="yes":

            stay=self.stand(hand)[0]

            #determine if hand is bust
            if stay==True:
                run="no"
            #get another card and re-run stand function
            else:
                hand.add_card()
        #Only return 22 if bust
        if hand.total >22:
            hand.total=22
        return hand.cards


def main():
    """creates a CSV file containing the percent of player wins based on player
    and dealer Strategy

    Parameters:
        None
    Returns:
        Blackjack.CSV : percent of player wins based on strategy

"""
    #open CSV writer
    with open('blackjack.csv', 'w', newline='') as csvfile:
        percentwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        #initialize variables
        labels=[]
        stand_on=(True, False)
        total_simulations=int(sys.argv[1])
        #create header
        for stand_on_value in range(13,21):

            for stand_on_soft in (stand_on):
                if stand_on_soft==True:
                    strategy='S'
                else:
                    strategy='H'
                labels+=[strategy+str(stand_on_value)]
        percentwriter.writerow(["P-Strategy"]+ labels)
        #loop through all the possible player and dealer strategies
        for stand_on_value in range(13,21):
            for stand_on_soft in (stand_on):
                if stand_on_soft==True:
                    strategy='S'
                else:
                    strategy='H'

                percent_list=["P-"+strategy+str(stand_on_value)]

                list_wins=[]

                for dealer_stand_on_value in range(13,21):

                    for dealer_stand_on_soft in (stand_on):
                        #initiate variables
                        num_simulations=int(sys.argv[1])

                        wins=0
                        #run the simulation based on num_simulations
                        while num_simulations > 0:
                            #deal to the player
                            deal=Strategy(stand_on_value, stand_on_soft)
                            cards=deal.play()
                            check=Hand(cards)

                            if check.is_bust() ==True:
                                #if bust player loses
                                num_simulations=num_simulations-1

                            else:
                                #deal to the dealer
                                dealer_deal=Strategy(dealer_stand_on_value, dealer_stand_on_soft)
                                dealer_cards=dealer_deal.play()
                                dealer_check=Hand(dealer_cards)


                                if dealer_check.is_bust()==True:
                                    #if the dealer is bust, player wins
                                    wins=wins+1
                                    num_simulations=num_simulations-1
                                    continue

                                if check.score()[0]==dealer_check.score()[0]:
                                    #if player and dealer tie
                                    if check.is_blackjack()==True and dealer_check.is_blackjack()==False:
                                        #if player gets blackjack, player wins
                                        wins=wins+1
                                        num_simulations=num_simulations-1
                                        continue

                                    else:
                                        #if dealer gets blackjack or just tie, player loses
                                        num_simulations=num_simulations-1
                                        continue

                                if check.is_blackjack()==True:
                                    #if player gets blackjack, player wins
                                    wins=wins+1
                                    num_simulations=num_simulations-1
                                    continue

                                if dealer_check.is_blackjack()==True:
                                    #if dealer gets blackjack, player loses
                                    num_simulations=num_simulations-1
                                    continue

                                if check.score()[0]>dealer_check.score()[0]:
                                    #if player has a higher total than dealer, player wins
                                    wins=wins+1
                                    num_simulations=num_simulations-1
                                    continue

                                else:
                                    #any other outcome is a player loss
                                    num_simulations=num_simulations-1
                                    continue


                        list_wins+=[wins]
                #convert list of wins into percentage
                for wins in list_wins:
                    percent=(100*(wins/total_simulations))
                    rounded_percent = round(percent, 2)
                    percent_list+=[rounded_percent]
                #add percentages to CSV
                percentwriter.writerow(percent_list)



if __name__=='__main__':
    main()
