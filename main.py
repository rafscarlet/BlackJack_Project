from art import logo
import random
import os

A=11
J=Q=K=10
cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]                               

player_blackjack=False
player_bust=False
dealer_blackjack=False
dealer_bust=False
theEnd=False
another='a'

def calc_score(hand:list): 
    blackjack=False
    bust=False

    if hand==[10,11] or hand==[11,10]:    
        blackjack=True
    
    score=sum(hand)
    
    if 11 in hand and score>21:
        hand[hand.index(11)]=1
        score=sum(hand)
    if score>21:
        bust=True

    return score, blackjack, bust


def computer_play(hand:list):
    #Computer draws cards as long as his sum is not bigger than 16 (also if sum>21 and he has an ace, the ace counts as 1)
    score=sum(hand)
    while score<=16:
        hand.append(random.choice(cards))
        score=calc_score(hand)[0]
    return hand 


def results(player_cards, dealer_cards):
    #Checks every condition and prints the final result of the game

    player_score, player_blackjack, player_bust = calc_score(my_cards)
    dealer_score, dealer_blackjack, dealer_bust = calc_score(dealer_cards)
    print(f'    Your final hand is {player_cards} with a score of {player_score}')
    print(f'    The dealer\'s final hand is {dealer_cards} with a score of {dealer_score}\n')

    #Blackjacks (if the dealer has a blackjack he wins in any occasion)
    if dealer_blackjack and not player_blackjack:
        print('You lose! The dealer got a BlackJack... How unlucky!🥺')
    elif dealer_blackjack and player_blackjack:
        print('You lose! The dealer also got a BlackJack!🥺')
    elif player_blackjack and not dealer_blackjack:
        print('You got a BlackJack! You Win!😎')
    #Busts (going over 21)
    elif player_bust:
        print('You busted! You lose...🥺')
    elif dealer_bust:
        print('The dealer went over! You win!😎')
    #Draw
    elif player_score==dealer_score:
        print('It\'s a draw!😒')
    #Win
    elif player_score>dealer_score:
        print('You win!😎')
    #Loss
    else:
        print('You lose...🥺')
    # print('\n')
    


#-------------------------GAME START----------------------------#

while not theEnd:

    if input(f'\nReady for {another} game of BlackJack? 🤩 ( Y=Yes / N=No ) ').lower() == 'y':
        os.system('cls')
        print(logo)
        isEnd=False
        hit=True
    else:
        isEnd=True
        print('Have a nice day!🙂')
        exit()

    # #generate players' cards
    my_cards=[random.choice(cards), random.choice(cards)]
    dealer_cards=[random.choice(cards), random.choice(cards)]

    # my_cards=[11,10]
    # # dealer_cards=[11,7]

    #check for blackjacks
    my_score, player_blackjack, player_bust=calc_score(my_cards)
    dealer_score, dealer_blackjack, dealer_bust=calc_score(dealer_cards)

    if dealer_blackjack or player_blackjack:
        #Game Ends
        hit=False
        results(my_cards,dealer_cards)   

    while hit:
        #demonstrate hand, score and ask if they want another hit
        my_score, player_blackjack, player_bust = calc_score(my_cards)
        dealer_score, dealer_blackjack, dealer_bust = calc_score(dealer_cards)
        print(f'\n    Your cards: {str(my_cards)} - - - Current score: {my_score}')
        print(f'    Dealer\'s first card is: {dealer_cards[0]}')
        moreCards=input('\nWant another card? (Type "h" to hit or "p" to pass) ')

        #if they choose pass
        if moreCards=='p':
            #Game Ends
            hit=False 
            #Computer plays
            dealer_cards=computer_play(dealer_cards)
            dealer_score, dealer_blackjack, dealer_bust=calc_score(dealer_cards)
            #Announce the winner (or draw)
            results(my_cards,dealer_cards)
            
            
        #if they choose hit    
        elif moreCards=='h':
            #New Card
            print('\n-----Here is your new card!-----\n')
            my_cards.append(random.choice(cards))
            my_score, player_blackjack, player_bust=calc_score(my_cards)
            
            if my_score>21:
                hit=False
                results(my_cards,dealer_cards)
            
    another='another'


