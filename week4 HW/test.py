from collections import namedtuple
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

print(stand(17,True,[1,1]))
