def score(cards):
    soft_ace_count=0

    for index,value in enumerate(cards):
        if value >10:
            cards[index]=10

    total=sum(cards)


    if (total<=11) and (1 in cards):
        total=total + 10
        soft_ace_count=1

    print(total)
    return (total, soft_ace_count)

def stand(stand_on_value, stand_on_soft, cards):
    total,soft_ace_count = score(cards)
    if total < stand_on_value:
        #hit
        print("F")
        return False

    if total== stand_on_value:
        print("yes")
        if stand_on_soft==True:

            #stand
            print("T")
            return True

        if stand_on_soft==False:
            if soft_ace_count==0:
                #stand
                print("T")
                return True
            if soft_ace_count==1:
                #hit
                print("F")
                return False
    if total > stand_on_value:
        #stand
        print("T")
        return True
print(stand(17, False, [6,1]))
