from art import logo
import random
import os

A=11
J=Q=K=10
cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]                               
# print(K)
                
player_bust=False
dealer_bust=False
player_blackjack=False
dealer_blackjack=False
hit=True
theEnd=False

def computer_play(hand:list):
    #Computer draws cards as long as his sum is not bigger than 16 (also if sum>21 and he has an ace, the ace counts as 1)
    score=sum(hand)
    while score<=16:
        hand.append(random.choice(cards))
        score=sum(hand)
    if 11 in hand and score>21:
        my_cards[my_cards.index(11)]=1
        score=sum(hand)
    return hand

def results(player_cards,dealer_cards):
    player_score=sum(player_cards)
    dealer_score=sum(dealer_cards)
    print('\n')
    print(f'    Your final hand is {player_cards} with a score of {player_score}')
    print(f'    The dealer\'s final hand is {dealer_cards} with a score of {dealer_score}\n')

    

#-----------------------GAME START----------------------------#

while not theEnd:

    if input('Ready for a game of BlackJack? 🤩 ( Y=Yes / N=No ) ').lower() == 'y':
        os.system('cls')
        print(logo)
        isEnd=False
        hit=True
    else:
        isEnd=True
        print('Have a nice day!🙂')
        exit()

    # #generate players' cards
    # my_cards=[random.choice(cards), random.choice(cards)]
    # dealer_cards=[random.choice(cards), random.choice(cards)]

    my_cards=[10,2]
    dealer_cards=[10,11]

    #check for blackjacks
    if dealer_cards==[10,11] or dealer_cards==[11,10]:
        dealer_blackjack=True
    if my_cards==[11,10] or my_cards==[10,11]:
        player_blackjack=True

    if dealer_blackjack or player_blackjack:
        #Game Ends
        hit=False
        #If the dealer has a blackjack he wins in any occasion
        if dealer_blackjack and not player_blackjack:
            result='You lose! The dealer got a BlackJack... How unlucky!🥺'
        elif dealer_blackjack and player_blackjack:
            result='You lose! The dealer also got a BlackJack!🥺'
        else:
            result='You got a BlackJack! You Win!😎'

        results(my_cards,dealer_cards)   
        print(result)


    while hit:
        #demonstrate hand, score and ask if they want another hit
        my_score=sum(my_cards)
        dealer_score=sum(my_cards)
        print(f'\n    Your cards: {str(my_cards)} - - - Current score: {my_score}')
        print(f'    Dealer\'s first card is: {dealer_cards[0]}')
        moreCards=input('\nWant another card? (Type "h" to hit or "p" to pass) ')

        #if they choose pass
        if moreCards=='p':
            #Game Ends
            hit=False 
            #Computer plays
            dealer_cards=computer_play(dealer_cards)
            dealer_score=sum(dealer_cards)
            if dealer_score>21:
                dealer_bust=True

            #Announce the winner (or draw)
            results(my_cards,dealer_cards)
            if my_score>dealer_score:
                print('You win!😎')
            elif my_score==dealer_score:
                print('It\'s a draw!😒')
            else:
                if dealer_bust==True:
                    print('The dealer went over! You win!😎')
                else:
                    print('You lose...🥺')
            
            
        #if they choose hit    
        elif moreCards=='h':
            #New Card
            print('-----Here is your new card!-----')
            my_cards.append(random.choice(cards))
            my_score=sum(my_cards)

            #Player Busted
            if my_score>21:
                #make aces count as 1 instead of 11
                if 11 in my_cards:
                    my_cards[my_cards.index(A)]=1
                    my_score=sum(my_cards)
                else:
                    player_bust=True
                    results(my_cards,dealer_cards)
                    print('You busted! You lose...🥺')
                    hit=False


            
            #If player hits 21 the game ends
            elif my_score==21:
                dealer_cards=computer_play(dealer_cards)
                results(my_cards,dealer_cards)
                print('You win!😎')
                hit=False


            
                


