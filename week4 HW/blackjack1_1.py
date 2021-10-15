import random
from collections import namedtuple
import sys

#adds random card to hand
def get_card():
    return random.randint(1,13)


def score(cards):
    """Counts the total value of the cards in the hand and the number of soft
    aces
    Parameters:
        cards: A list of the cards in a single blackjack hand

    Returns:
        total: Total value of the cards in the hand
        soft_ace_count: The number of aces counted as 11 in the hand
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
    Score = namedtuple('Score', ['total', 'soft_ace_count'])
    S= Score(total,soft_ace_count)
    return S

def stand(stand_on_value, stand_on_soft, cards):
    """Determines if the player should stand or hit based on their current hand
    Parameters:
        stand_on_value: the integer to determine if they should stand
        stand_on_soft: A boolean representing stand on soft or stand on hard
        cards: A list of the cards in a single blackjack hand

    Returns:
        total: Total value of the cards in the hand
        soft_ace_count: The number of aces counted as 11 in the hand
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
    Stand = namedtuple('Stand', ['stand', 'total'])
    S= Stand(stand,total)
    return S




def play_hand(stand_on_value, stand_on_soft):
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
    if total >22:
        total=22
    return total

def main():
    """Runs the simulater a specified number of times to determine the percent
    of bust hands
    Parameters:
        none
    Returns:
        percent: The percent of hands that went bust out of the total number of
        simulations
    """
    #basic validation on the arguments and raising a ValueError exception
    try:
        num_simulations=int(sys.argv[1])
    except ValueError:
        print("Number of simulations must be an integer")
    try:
        stand_on_value=int(sys.argv[2])
    except ValueError:
        print("Stand on value must be an integer")
    # define variables
    num_simulations=int(sys.argv[1])
    total_simulations=int(sys.argv[1])
    stand_on_value=int(sys.argv[2])
    if sys.argv[3].lower()=='soft':
        stand_on_soft=True
    if sys.argv[3].lower()=='hard':
        stand_on_soft=False

    bust=0

    #check that acceptable values were picked
    if num_simulations < 0:
        raise Exception("Number of simulatuions must be more than zero")
    if stand_on_value< 1 or stand_on_value>20:
        raise Exception("Stand on value must be between 1 and 20")

    #run the simulation the specified number of times
    while num_simulations > 0:
        total = play_hand(stand_on_value, stand_on_soft)
        if total == 22:
            bust+=1
        num_simulations=num_simulations-1

        #calculate the percent of bust hands
        percent=float((bust/total_simulations)*100)

    print(percent)
    return percent


if __name__=='__main__':
    main()
