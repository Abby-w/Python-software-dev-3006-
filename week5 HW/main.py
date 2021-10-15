list_wins=[]
    wins=0
    for dealer_stand_on_value in range(13,22):
        #loop through stand on soft and stand on hard
        for dealer_stand_on_soft in (stand_on):

            while num_simulations > 0:
                deal=Strategy(stand_on_value, stand_on_soft)
                cards=deal.play()
                check=Hand(cards)
                print("player",check)
                if check.is_bust() ==True:

                    num_simulations=num_simulations-1

                else:
                    dealer_deal=Strategy(dealer_stand_on_value, dealer_stand_on_soft)
                    dealer_cards=dealer_deal.play()
                    dealer_check=Hand(cards)
                    print("dealer",dealer_check)
                    if dealer_check.is_bust()==True:
                        wins+=1
                        num_simulations=num_simulations-1

                    if check.score()[0]==dealer_check.score()[0]:
                        if check.is_blackjack()==True and dealer_check.is_blackjack()==False:
                            wins+=1
                            num_simulations=num_simulations-1

                        if check.is_blackjack()==False and dealer_check.is_blackjack()==True:
                            num_simulations=num_simulations-1

                        else:
                            num_simulations=num_simulations-1

                    if check.is_blackjack()==True:
                        wins+=1
                        num_simulations=num_simulations-1

                    if dealer_check.is_blackjack()==True:
                        num_simulations=num_simulations-1

                    if check.score()[0]>dealer_check.score()[0]:
                        wins+=1
                        num_simulations=num_simulations-1

                    else:
                        num_simulations=num_simulations-1


            list_wins+=[wins]
    print(list_wins)

                #write the percent of time the value occurs into the CSV
    for wins in list_wins:
        percent=(100*wins/total_simulations)
        percent_list+=[percent]
        percentwriter.writerow(percent_list)
