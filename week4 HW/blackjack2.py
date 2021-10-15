import random
from collections import namedtuple
from collections import defaultdict
import sys
import csv
Stand = namedtuple('Stand', ['stand', 'total'])
Score = namedtuple('Score', ['total', 'soft_ace_count'])
#adds random card to hand
def get_card():
    return random.randint(1,13)


def score(cards):
    """Counts the total value of the cards in the hand and the number of soft
    aces
    Parameters:
        cards: A list of the cards in a single blackjack hand

    Returns:
        S= namedtuple of the card total and the soft ace coount
    """
    #initialize variables
    soft_ace_count=0
    #change the jack, queen and king cards to a value of 10
    for index,value in enumerate(cards):
        if value >10:
            cards[index]=10
    #calculate the total value
    total=sum(cards)
    #account for possible soft aces in the hand
    if (total<=11) and (1 in cards):
        total=total + 10
        soft_ace_count=1
    #add information to the named tuple
    S= Score(total,soft_ace_count)
    return S

def stand(stand_on_value, stand_on_soft, cards):
    """Determines if the player should stand or hit based on their current hand
    Parameters:
        stand_on_value: the integer to determine if they should stand
        stand_on_soft: A boolean representing stand on soft or stand on hard
        cards: A list of the cards in a single blackjack hand

    Returns:
        S= namedtuple of boolean whether to stand or not and the total value of
        the cards
    """
    #initialize variable
    total,soft_ace_count = score(cards)
    #case one: total is less than the stand on value -- always hit
    if total < stand_on_value:
        stand = False
    #case two: total is equal than the stand on value
    if total== stand_on_value:
        if stand_on_soft==True:
            #stand
            stand= True
        if stand_on_soft==False:
            if soft_ace_count==0:
                #stand
                stand = True
            if soft_ace_count==1:
                #hit
                stand =  False
    #case three: total is greater than the stand on value  --always stand
    if total > stand_on_value:
        stand = True
    #add information to the named tuple
    S= Stand(stand,total)
    return S




def play_hand(stand_on_value, stand_on_soft):
    """runs a single hand to completion
    Parameters:
        stand_on_value: Integer between 13 and 21
        stand_on_soft: Boolean, whether to stand on soft or stand on hard
    Returns:
        total:The total value of cards at the end of a hand
    """
    #set the starting hand
    cards=[]
    cards+=[get_card()]
    cards+=[get_card()]
    run="yes"
    #check the total and determine whether to hit or stand
    while run=="yes":
        total,soft_ace_count = score(cards)
        stay=stand(stand_on_value, stand_on_soft, cards)[0]
        #determine if hand is bust
        if stay==True:
            run="no"
        #get another card and re-run stand function
        else:
            cards+=[get_card()]
    #Only return 22 if bust
    if total >22:
        total=22
    return total

def main():
    """Runs the simulater a specified number of times to determine the percent
    of bust hands per strategy
    Parameters:
        none
    Returns:
        sys.stdout: blackjack.csv as a table of the percent of simulations
        resulting in a specific value per strategy
    """
    #open the file to write the CSV to
    with open('blackjack.csv', 'w', newline='') as csvfile:
        percentwriter = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        percentwriter.writerow(['Strategy', '13', '14', '15', '16', '17', '18', '19', '20', '21', 'BUST'])

        stand_on=(True, False)
        #loop through the stand on values
        for stand_on_value in range(13,22):
            #loop through stand on soft and stand on hard
            for stand_on_soft in (stand_on):
                if stand_on_soft==True:
                    strategy='S'
                else:
                    strategy='H'
                #define variables
                total_simulations=int(sys.argv[1])
                num_simulations=int(sys.argv[1])
                percent_list=[strategy+str(stand_on_value)]
                list=[]
                dictionary = defaultdict(int, {13: 0, 14: 0, 15: 0, 16: 0,
                17: 0, 18:0, 19:0, 20:0, 21:0, 22:0})

                #run the simulation the specified number of times
                while num_simulations > 0:
                    total = play_hand(stand_on_value, stand_on_soft)
                    dictionary[total] += 1
                    num_simulations=num_simulations-1

                #redefine value of 22 as BUST
                dictionary['BUST'] = dictionary.pop(22)
                #put count in a list
                list_values=[*dictionary.values()]
                #write the percent of time the value occurs into the CSV
                for value in list_values:
                    percent=(100*value/total_simulations)
                    percent_list+=[percent]
                percentwriter.writerow(percent_list)


if __name__=='__main__':
    main()
