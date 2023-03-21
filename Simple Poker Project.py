
import random

def deck():
    deck_dictionary = {}
    infile = open('deck52.txt', 'r')
    for line in infile:
        suite = line.strip()
        deck_dictionary[suite] = []
        line = infile.readline().strip()
        while line != '':
            deck_dictionary[suite].append(line)
            line = infile.readline().strip()
    return deck_dictionary



def deal_card(deck_dictionary):
    suite = random.randrange(1,5)
    if suite == 1:
        suite = 'C'
    elif suite == 2:
        suite = 'D'
    elif suite == 3:
        suite = 'H'
    elif suite == 4:
        suite = 'S'
    indicator = random.randrange(0,len(deck_dictionary[suite]))
    value = deck_dictionary[suite][indicator]
    del deck_dictionary[suite][indicator]
    return f'{value}{suite}', deck_dictionary

def intro():
    #welcome information
    #starting money 200
    #player will bet first
    BUY_IN=10
    print('Welcome to Kristof and Carter\'s Poker Game')
    print('We hope you enjoy playing!')
    print()
    money = int(input('How much should each player start with? '))
    while money<=10:
        print('To account for a buy in, please enter a starting amount greater than $10')
        money = int(input('How much should each player start with? '))
    while money%5 != 0:
        print('For ease of calculation, please make starting money a multiple of 5')
        money = int(input('How much should each player start with? '))
    print('Betting will take place in increments of $5')
    print()
    return money, BUY_IN



def main ():
    #get pot and starting money
    money, BUY_IN = intro()
    player_money = money
    computer_money = money

    again=1
    
    #pocket deal betting
    #deal both players 2 cards
    while again!=2:
        #load dictionary and intro
        deck_dictionary = deck()
        
        pot = (BUY_IN)*2
        player_money -= BUY_IN
        computer_money -= BUY_IN
        print(f'After the ${BUY_IN} buy in:')
        print(f'You have ${player_money}')
        print(f'The computer has ${computer_money}')
        print(f'The pot is at ${BUY_IN*2}')
        print()
        print('To start, you will bet first')
        card1, deck_dictionary = deal_card(deck_dictionary)
        card2, deck_dictionary = deal_card(deck_dictionary)
        card3, deck_dictionary = deal_card(deck_dictionary)
        card4, deck_dictionary = deal_card(deck_dictionary)
        player_hand = [card1,card2]
        computer_hand = [card3,card4]
        print(f'Your pocket is the {player_hand[0]} and the {player_hand[1]}')
        #print(f'The computer\'s pocket is the {computer_hand[0]} and the {computer_hand[1]}')
        print()

        #player bet and money updating
        #player bet (0, player money) or fold



       #   PRE BETTING ROUND



        player_money, computer_money, pot, folded = round(player_money, computer_money, pot)

        if folded == 'p':
            print('You have folded')
            print(f'The computer wins the pot of ${pot}')
            computer_money+=pot
                
        elif folded == 'c':
            print('The computer has folded')
            print(f'You win the pot of ${pot}')
            player_money+=pot
                
        elif player_money == 0 or computer_money == 0:
            print('Since at least 1 player has $0, the rest of the cards will now be dealt')
            pool = []
            for i in range(5):
                card, deck_dictionary = deal_card(deck_dictionary)
                pool.append(card)
            print('Your hand plus the community cards:')
            print()
            for card in player_hand:
                print(f'{card}', end = ' ')
            print('\t', end = '')
            for card in pool:
                print(f'{card}', end = ' ')
            print()
            print()
            winner=showdown(pool, player_hand, computer_hand)
            if winner=='Player':
                player_money+=pot
            elif winner=='Computer':
                computer_money+=pot



            #  THE FLOP ROUND 



                
        else:
            print('Continuing to the next round ...')
            print()
            #flop betting (3 community, player first)
            #deal 3 community cards
            pool = []
            for i in range(3):
                card, deck_dictionary = deal_card(deck_dictionary)
                pool.append(card)
            print(f'The first 3 community cards are the {pool[0]}, the {pool[1]}, and the {pool[2]}')
            #show player all available cards (no order)
            print('Your hand plus the community cards:')
            print()
            for card in player_hand:
                print(f'{card}', end = ' ')
            print('\t', end = '')
            for card in pool:
                print(f'{card}', end = ' ')
            print()
            print()
            
            player_money, computer_money, pot, folded = round(player_money, computer_money, pot)
            if folded == 'p':
                print('You have folded')
                print(f'The computer wins the pot of ${pot}')
                computer_money+=pot
                    
            elif folded == 'c':
                print('The computer has folded')
                print(f'You win the pot of ${pot}')
                player_money += pot
                    
            elif player_money == 0 or computer_money == 0:
                print('Since at least 1 player has $0, the rest of the cards will now be dealt')
                for i in range(2):
                    card, deck_dictionary = deal_card(deck_dictionary)
                    pool.append(card)
                print('Your hand plus the community cards:')
                print()
                for card in player_hand:
                    print(f'{card}', end = ' ')
                print('\t', end = '')
                for card in pool:
                    print(f'{card}', end = ' ')
                print()
                print()
                winner=showdown(pool, player_hand, computer_hand)
                if winner=='Player':
                    player_money+=pot
                elif winner=='Computer':
                    computer_money+=pot




            # FIRST COMMUNITY CARD

                
                
            else:
                print('Continuing to the next round ...')
                print()
                #turn betting
                #deal 1 community card
                card, deck_dictionary = deal_card(deck_dictionary)
                pool.append(card)
                print(f'The next community card is the {card}')
                #show player all available cards (no order)
                print('Your hand plus the community cards:')
                for card in player_hand:
                    print(f'{card}', end = ' ')
                print('\t', end = '')
                for card in pool:
                    print(f'{card}', end = ' ')
                print()
                print()
                
                player_money, computer_money, pot, folded = round(player_money, computer_money, pot)
                if folded == 'p':
                    print('You have folded')
                    print(f'The computer wins the pot of ${pot}')
                    computer_money+=pot
                        
                elif folded == 'c':
                    print('The computer has folded')
                    print(f'You win the pot of ${pot}')
                    player_money += pot
                        
                elif player_money == 0 or computer_money == 0:
                    print('Since at least 1 player has $0, the rest of the cards will now be dealt')
                    for i in range(1):
                        card, deck_dictionary = deal_card(deck_dictionary)
                        pool.append(card)
                    print('Your hand plus the community cards:')
                    print()
                    for card in player_hand:
                        print(f'{card}', end = ' ')
                    print('\t', end = '')
                    for card in pool:
                        print(f'{card}', end = ' ')
                    print()
                    print()
                    winner=showdown(pool, player_hand, computer_hand)
                    if winner=='Player':
                        player_money+=pot
                    elif winner=='Computer':
                        computer_money+=pot





            # SECOND COMMUNITY CARD



                    
                else:
                    print('Continuing to the next round ...')
                    print()
                    #river betting
                    #deal 1 community card
                    card, deck_dictionary = deal_card(deck_dictionary)
                    pool.append(card)
                    print(f'The final community card is the {card}')
                    #show player all available cards (no order)
                    print('Your hand plus the community cards:')
                    for card in player_hand:
                        print(f'{card}', end = ' ')
                    print('\t', end = '')
                    for card in pool:
                        print(f'{card}', end = ' ')
                    print()
                    print()
                    player_money, computer_money, pot, folded = round(player_money, computer_money, pot)
                    if folded == 'p':
                        print('You have folded')
                        print(f'The computer wins the pot of ${pot}')
                        computer_money+=pot

                    elif folded == 'c':
                        print('The computer has folded')
                        print(f'You win the pot of ${pot}')
                        player_money += pot

                    else:
                        print('The showdown will now commence')
                        winner=showdown(pool, player_hand, computer_hand)
                        if winner == 'Player':
                            player_money+=pot
                        elif winner == 'Computer':
                            computer_money+=pot
                        elif winner == 'Tie':
                            player_money+=(pot/2)
                            player_money+=(pot/2)
                        
        print()              
        if computer_money==0:
            print('The computer has reached $0')
            print('Congratulations! You win!')
            again=2
        elif player_money==0:
            print('You have reached $0')
            print('Unfortunately, you lose ...')
            again=2
        else:
            print('Yes - 1')
            print('No - 2')
            again=int(input('Would you like to play another round? '))
        if again == 0:
            print()
            print('Computer possible hand: ')
            for card in computer_hand:
                print(f'{card}', end = ' ')
            print('\t', end = '')
            for card in pool:
                print(f'{card}', end = ' ')
            print()
            print()
            again = int(input('Would you like to play another round? '))
        while again!=1 and again!=2:
            print('Please choose an option from the menu')
            print()
            print('Yes - 1')
            print('No - 2')
            again=int(input('Would you like to play another round? '))
            print()

            




def round(player_money, computer_money, pot):
    folded = False
    min_bet = 0
    player_bet, player_money, pot, folded = player_decision(player_money, pot, min_bet)
    if folded == 'p':
        #player folds
        return player_money, computer_money, pot, folded
    else:
        folded = random.randint(1,20)
        if folded == 1:
            #computer folds
            folded = 'c'
            return player_money, computer_money, pot, folded
        else: #get computer's bet
            if player_bet >= computer_money:
                computer_bet = computer_money
                computer_money = 0
                pot += computer_bet
                print(f'The computer must now go all in, betting ${computer_bet} to match you')
                print()
                print(f'You have ${player_money}')
                print(f'The computer has ${computer_money}')
                print(f'The pot is now at ${pot}')
                print()
            else:
                computer_max = player_bet+20
                computer_bet = random.randrange(player_bet, computer_max,5)
                computer_money -= computer_bet
                pot += computer_bet
                print(f'The computer has bet ${computer_bet}')
                print()
                print(f'You have ${player_money}')
                print(f'The computer has ${computer_money}')
                print(f'The pot is at ${pot}')
                print()
                if computer_bet > player_bet:
                    print(f'You must bet at least ${computer_bet-player_bet} to match the computer')
                    min_bet = computer_bet-player_bet
                    #To continue, player must at least match the computer
                    player_bet, player_money, pot, folded = player_decision(player_money, pot, min_bet)
                    if folded == 'p':
                        return player_money, computer_money, pot, folded
                    elif player_bet > computer_bet:
                        print(f'You bet ${player_bet}')
                        if player_bet >= computer_money:
                            computer_bet = computer_money
                            computer_money = 0
                            print(f'The computer must now go all in, betting ${computer_bet} to match you')
                            print()
                        else:
                            print(f'The computer matches your bet with ${player_bet}')
                            computer_money -= player_bet
                            print()
                        pot += player_bet + computer_bet
                        print(f'You have ${player_money}')
                        print(f'The computer has ${computer_money}')
                        print(f'The pot is at ${pot}')
                        print()
                    else: #player has matched computer
                        print(f'You have ${player_money}')
                        print(f'The computer has ${computer_money}')
                        print(f'The pot is at ${pot}')
                        print()
            return player_money, computer_money, pot, folded
            #continue to next round

        
def menu_of_options():
    choice_list = ['1 - Bet','2 - Fold']
    print('Your choices are:')
    for item in choice_list:
        print(item)
    go = False
    while go == False:
        try:
            choice = int(input('Your choice? '))
            while choice < 1 or choice > 2:
                print('Please choose an option from the menu')
                print('Your choices are:')
                for item in choice_list:
                    print(item)
                choice = int(input('Your choice? '))
            return choice
        except ValueError:
            print('Only integer input accepted')
            print('Your choices are: ')
            for item in choice_list:
                    print(item)


def player_decision(player_money, pot, min_bet):
    choice = menu_of_options()
    if choice == 2:
        #player folds
        player_bet = 0
        folded = 'p'
    else:
        folded = False
        if min_bet > player_money:
            #You've been forced to go all in
            player_bet = player_money
        elif min_bet > 0:
            #validate player's bet
            #You must bet at least min_bet
            player_bet = int(input('How much would you like to bet? '))
            while player_bet < min_bet:
                print(f'You must bet at least ${min_bet}')
                player_bet = int(input('How much would you like to bet? '))
            while player_bet%5 != 0:
                print('Please enter a multiple of 5 as your bet')
                player_bet = int(input('How much would you like to bet? '))
        else: #min_bet == 0
            player_bet = int(input('How much would you like to bet? '))
            while player_bet > player_money or player_bet < 0:
                print(f'You must bet between $0 and ${player_money}')
                player_bet = int(input('How much would you like to bet? '))
            while player_bet%5 != 0:
                print('Please enter a multiple of 5 as your bet')
                player_bet = int(input('How much would you like to bet? '))
        player_money -= player_bet
        pot += player_bet
        print()
        print(f'You added ${player_bet} to make the pot ${pot}')
        print()
    return player_bet, player_money, pot, folded




#    BELOW IS LITERALLY ALL HAND EVALUATION FUNCTIONS








def showdown(pool, player_hand, computer_hand):
    poutcome, pbest_hand, phrase1 = card_evaluation(pool, player_hand)
    coutcome, cbest_hand, phrase2 = card_evaluation(pool, computer_hand)
    #
    #
##    for card in computer_hand:
##        print(f'{card}', end = ' ')
##    print('\t', end = '')
##    for card in pool:
##        print(f'{card}', end = ' ')
    print()
    #
    #

    #Turn player and computer best hands into formatted strings for result printing
    pstring_best_hand = ''
    for card in pbest_hand:
        if card[-3:-1] == '10':
            pstring_best_hand += f'{str(card)} '
        else:
            pstring_best_hand += f' {str(card)} '

    cstring_best_hand = ''
    for card in cbest_hand:
        if card[-3:-1] == '10':
            cstring_best_hand += f'{str(card)} '
        else:
            cstring_best_hand += f' {str(card)} '

    #Print player and computer best hands
    print(f'Your best hand: {pstring_best_hand:2}  {phrase1}')
    print(f'Comp best hand: {cstring_best_hand:2}  {phrase2}\n')
    #Player wins
    if poutcome>coutcome:
        print(f'You win! Your {phrase1} beats the computer\'s {phrase2}')
        return 'Player'
    #Computer wins
    elif coutcome>poutcome:
        print(f'The computer wins. It\'s {phrase2} beat your {phrase1}')
        return 'Computer'
    #Tie resolution
    elif coutcome==poutcome:
        if poutcome == 1: #High card --> next --> next --> etc. --> tie
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
            cbest_hand_list.sort()
            pbest_hand_list.sort()

            if cbest_hand_list[-1]>pbest_hand_list[-1]:
                print(f'Computer wins with the highest unshared card')
                return 'Computer'
            elif pbest_hand_list[-1]>cbest_hand_list[-1]:
                print(f'You win with the highest unshared card')
                return 'Player'
            elif cbest_hand_list[-2]>pbest_hand_list[-2]:
                print(f'Computer wins with the highest unshared card')
                return 'Computer'
            elif pbest_hand_list[-2]>cbest_hand_list[-2]:
                print('You win with the highest unshared card')
                return 'Player'
            elif cbest_hand_list[-3]>pbest_hand_list[-3]:
                print(f'Computer wins with the highest unshared card')
                return 'Computer'
            elif pbest_hand_list[-3]>cbest_hand_list[-3]:
                print('You win with the highest unshared card')
                return 'Player'
            elif cbest_hand_list[-4]>pbest_hand_list[-4]:
                print(f'Computer wins with the highest unshared card')
                return 'Computer'
            elif pbest_hand_list[-4]>cbest_hand_list[-4]:
                print('You win with the highest unshared card')
                return 'Player'
            elif cbest_hand_list[-5]>pbest_hand_list[-5]:
                print(f'Computer wins with the highest unshared card')
                return 'Computer'
            elif pbest_hand_list[-5]>cbest_hand_list[-5]:
                print('You win with the highest card')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
              
            
        if poutcome == 2: #Pair --> highest pair --> highest of rest --> tie
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))

            if cbest_hand_list[0]>pbest_hand_list[0]:
                print('Computer wins with the highest valued pair')
                return 'Computer'
            elif pbest_hand_list[0]>cbest_hand_list[0]:
                print('You win with the highest valued pair')
                return 'Player'
            elif cbest_hand_list[2]>pbest_hand_list[2]:
                print('Computer wins with the highest unshared card after its pair')
                return 'Computer'
            elif cbest_hand_list[2]<pbest_hand_list[2]:
                print('You win with the highest unshared card after your pair')
                return 'Player'
            elif cbest_hand_list[3]>pbest_hand_list[3]:
                print('Computer wins with the highest unshared card after its pair')
                return 'Computer'
            elif cbest_hand_list[3]<pbest_hand_list[3]:
                print('You win with the highest unshared card after your pair')
                return 'Player'
            elif cbest_hand_list[4]>pbest_hand_list[4]:
                print('Computer wins with the highest unshared card after its pair')
                return 'Computer'
            elif cbest_hand_list[4]<pbest_hand_list[4]:
                print('You win with the highest unshared card after your pair')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
            
                        
        if poutcome == 3: #Two Pair --> highest pair1 --> highest pair 2 --> high card --> tie
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
            if cbest_hand_list[0]>pbest_hand_list[0]:
                print(f'Computer wins with the highest valued pair')
                return 'Computer'
            elif pbest_hand_list[0]>cbest_hand_list[0]:
                print(f'You win with the highest valued pair')
                return 'Player'
            elif cbest_hand_list[2]>pbest_hand_list[2]:
                print(f'Computer wins with the highest second pair')
                return 'Computer'
            elif pbest_hand_list[2]>cbest_hand_list[2]:
                print(f'You win with the highest second pair')
                return 'Player'
            elif cbest_hand_list[4]>pbest_hand_list[4]:
                print(f'Computer wins with the highest card after its pairs')
                return 'Computer'
            elif pbest_hand_list[4]>cbest_hand_list[4]:
                print(f'You win with the highest card after your pairs')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'




                
        if poutcome == 4: #Three of a Kind --> highest 3kind --> highest of rest --> tie
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
                        
            if cbest_hand_list[0]>pbest_hand_list[0]:
                print(f'Computer wins with the highest valued 3 of a kind')
                return 'Computer'
            elif pbest_hand_list[0]>cbest_hand_list[0]:
                print(f'You win with the highest valued 3 of a kind')
                return 'Player'
            elif cbest_hand_list[3]>pbest_hand_list[3]:
                print(f'Computer wins with the highest card after its 3 of a kind')
                return 'Computer'
            elif pbest_hand_list[3]>cbest_hand_list[3]:
                print(f'You win with the highest card after your 3 of a kind')
                return 'Player'
            elif cbest_hand_list[4]>pbest_hand_list[4]:
                print(f'Computer wins with the second highest card after its 3 of a kind')
                return 'Computer'
            elif pbest_hand_list[4]>cbest_hand_list[4]:
                print(f'You win with the second highest card after your 3 of a kind')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
            
            
            
        if poutcome == 5:   #Straight
            for card in pool:
                if card in pbest_hand:
                    pbest_hand.remove(card)
                elif card in cbest_hand:
                    cbest_hand.remove(card)
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
                        
            cbest_hand_list.sort
            pbest_hand_list.sort
            if cbest_hand_list[-1]>pbest_hand_list[-1]:
                print(f'Computer wins with the highest valued straight')
                return 'Computer'
            elif pbest_hand_list[-1]>cbest_hand_list[-1]:
                print('You win with the highest valued straight')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
                
        if poutcome == 6:   #Flush
            for card in pool:
                if card in pbest_hand:
                    pbest_hand.remove(card)
                elif card in cbest_hand:
                    cbest_hand.remove(card)
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
                        
            cbest_hand_list.sort
            pbest_hand_list.sort
            if cbest_hand_list[-1]>pbest_hand_list[-1]:
                print(f'The computer wins with the highest valued flush')
                return 'Computer'
            elif pbest_hand_list[-1]>cbest_hand_list[-1]:
                print('You win with the highest valued flush')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
                
        if poutcome == 7:   #Full house
            pbest_hand_list=[]
            cbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
            if cbest_hand_list[0]>pbest_hand_list[0]:
                print(f'Computer wins with the highest valued 3 of a kind in its full house')
                return 'Computer'
            elif pbest_hand_list[0]>cbest_hand_list[0]:
                print(f'You win with the highest valued 3 of a kind in your full house')
                return 'Player'
            elif cbest_hand_list[-1]>pbest_hand_list[-1]:
                print('Computer wins with the highest valued pair in its full house')
                return 'Computer'
            elif pbest_hand_list[-1]>cbest_hand_list[-1]:
                print('You win with the the highest valued pair in your full house')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
                        
            
        if poutcome == 8:   #Four of a kind
            pbest_hand_list=[]
            cbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
                        
            if cbest_hand_list[0]>pbest_hand_list[0]:
                print(f'Computer wins with the highest valued four of a kind')
                return 'Computer'
            elif pbest_hand_list[0]>cbest_hand_list[0]:
                print(f'You win with the highest valued four of a kind')
                return 'Player'
            elif cbest_hand_list[-1]>pbest_hand_list[-1]:
                print('Computer wins with the highest fifth card in its four of a kind')
                return 'Computer'
            elif pbest_hand_list[-1]>cbest_hand_list[-1]:
                print('You win with the highest fifth card in your four of a kind')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
            
        if poutcome == 9:   #straight flush
            for card in pool:
                if card in pbest_hand:
                    pbest_hand.remove(card)
                elif card in cbest_hand:
                    cbest_hand.remove(card)
            pbest_hand_list=[]
            for card in pbest_hand:
                if card[0]=='A':
                        num=14
                        pbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        pbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        pbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        pbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        pbest_hand_list.append(num)
                else: 
                        pbest_hand_list.append(int(card[0]))
            cbest_hand_list=[]
            for card in cbest_hand:
                if card[0]=='A':
                        num=14
                        cbest_hand_list.append(num)
                elif card[0]=='K':
                        num=13
                        cbest_hand_list.append(num)
                elif card[0]=='Q':
                        num=12
                        cbest_hand_list.append(num)
                elif card[0]=='J':
                        num=11
                        cbest_hand_list.append(num)
                elif len(card)==3:
                        num=10
                        cbest_hand_list.append(num)
                else: 
                        cbest_hand_list.append(int(card[0]))
                        
            cbest_hand_list.sort
            pbest_hand_list.sort
            if cbest_hand_list[-1]>pbest_hand_list[-1]:
                print(f'Computer wins with the highest card in its straight flush')
                return 'Computer'
            elif pbest_hand_list[-1]>cbest_hand_list[-1]:
                print('You win with the highest card in its straight flush')
                return 'Player'
            else:
                print('Both you and the computer have the same best hand')
                print('The pot will therefore be split between both of you')
                return 'Tie'
                
                    
        if poutcome == 10:  #Royal flush
            print('Both you and the computer have the same best hand')
            print('The pot will therefore be split between both of you')
            return 'Tie'
            
            
        


        
        


def card_evaluation(pool,hand):
    possible = pool+hand
  
    result, five_hand = royal_flush(pool,hand)
    if result == 10:
        return 10, five_hand, 'Royal Flush'
    else:
        result, five_hand = straight_flush(pool,hand)
        if result == 9:
            return 9,five_hand, 'Straight Flush'
        else:
            result, five_hand = four_of_a_kind(pool,hand)
            if result == 8:
                return 8, five_hand, 'Four of a Kind'
            else:
                result, five_hand = full_house(pool,hand)
                if result == 7:
                    return 7, five_hand, 'Full House'
                else:
                    result, five_hand = flush(pool,hand)
                    if result == 6:
                        return 6, five_hand, 'Flush'
                    else:
                        result, five_hand = straight(pool,hand)
                        if result == 5:
                            return 5, five_hand, 'Straight'
                        else:
                            result, five_hand = three_of_a_kind(pool,hand)
                            if result == 4:
                                return 4, five_hand, 'Three of a Kind'
                            else:
                                result, five_hand = two_pair(pool,hand)
                                if result == 3:
                                    return 3, five_hand, 'Two Pairs'
                                else:
                                    result, five_hand = pair(pool,hand)
                                    if result == 2:
                                        return 2, five_hand, 'One Pair'
                                    else:
                                        result, five_hand = high_card(pool, hand)
                                        return 1, five_hand, 'High Card'


def royal_flush(pool,hand):
    hearts  = []
    diamonds = []
    spades = []
    clubs = []
    inorder=False
    has_five=False
    isace=False
    possible = pool + hand
    for card in possible:
        if card[-1] == 'H':
            hearts.append(card)
        elif card [-1] == 'D':
            diamonds.append(card)
        elif card[-1] == 'S':
            spades.append(card)
        elif card[-1] == 'C':
            clubs.append(card)
    if len(hearts)>=5:
            has_five=True
            suit = 'H'
    elif len(diamonds)>=5:
            has_five=True
            suit = 'D'
    elif len(clubs)>=5:
            has_five=True
            suit = 'C'
    elif len(spades)>=5:
            has_five=True
            suit = 'S'
    else:
        has_five=False

        
    mylist=[]
    
    for card in possible:
            if card[0]=='A':
                    num=14
                    mylist.append(num)
            elif card[0]=='K':
                    num=13
                    mylist.append(num)
            elif card[0]=='Q':
                    num=12
                    mylist.append(num)
            elif card[0]=='J':
                    num=11
                    mylist.append(num)
            elif len(card)==3:
                    num=10
                    mylist.append(num)
            else: 
                    mylist.append(int(card[0]))
    
    mylist.sort()

    
    if int(mylist[1])==int(mylist[0])+1 and int(mylist[2])==int(mylist[1])+1 and int(mylist[3])==int(mylist[2])+1 and int(mylist[4])==int(mylist[3])+1:
            inorder=True
    elif int(mylist[2])==int(mylist[1])+1 and int(mylist[3])==int(mylist[2])+1 and int(mylist[4])==int(mylist[3])+1 and int(mylist[5])==int(mylist[4])+1:
            inorder=True
    elif int(mylist[3])==int(mylist[2])+1 and int(mylist[4])==int(mylist[3])+1 and int(mylist[5])==int(mylist[4])+1 and int(mylist[6])==int(mylist[5])+1:
            inorder=True
    else:
        inorder=False

    if mylist[-1]==14:
        isace=True
    else:
        isace=False

    five_hand = []
    if has_five==True and inorder==True and isace==True:
        values = ['A','K','Q','J','10']
        for card in values:
            five_hand.append(card + suit)
        return 10, five_hand
    else:
        return 0, possible




def straight_flush(pool,hand):
    hearts  = []
    diamonds = []
    spades = []
    clubs = []
    inorder=False
    has_five=False
    possible = pool + hand
    for card in possible:
        if card[-1] == 'H':
            hearts.append(card)
        elif card [-1] == 'D':
            diamonds.append(card)
        elif card[-1] == 'S':
            spades.append(card)
        elif card[-1] == 'C':
            clubs.append(card)
    if len(hearts)>=5:
            has_five=True
            suit = 'H'
    elif len(diamonds)>=5:
            has_five=True
            suit = 'D'
    elif len(clubs)>=5:
            has_five=True
            suit = 'C'
    elif len(spades)>=5:
            has_five=True
            suit = 'S'
    else:
        has_five=False

        
    mylist=[]
    
    for card in possible:
            if card[0]=='A':
                    num=14
                    mylist.append(num)
            elif card[0]=='K':
                    num=13
                    mylist.append(num)
            elif card[0]=='Q':
                    num=12
                    mylist.append(num)
            elif card[0]=='J':
                    num=11
                    mylist.append(num)
            elif len(card)==3:
                    num=10
                    mylist.append(num)
            else: 
                    mylist.append(int(card[0]))
    
    mylist.sort()

    
    if int(mylist[1])==int(mylist[0])+1 and int(mylist[2])==int(mylist[1])+1 and int(mylist[3])==int(mylist[2])+1 and int(mylist[4])==int(mylist[3])+1:
            inorder=True
    elif  int(mylist[2])==int(mylist[1])+1 and int(mylist[3])==int(mylist[2])+1 and int(mylist[4])==int(mylist[3])+1 and int(mylist[5])==int(mylist[4])+1:
            inorder=True
    elif  int(mylist[3])==int(mylist[2])+1 and int(mylist[4])==int(mylist[3])+1 and int(mylist[5])==int(mylist[4])+1 and int(mylist[6])==int(mylist[5])+1:
            inorder=True
    else:
        inorder=False

    
    values = mylist[-1:-6:-1]
    cards = []
    for value in values:
        if value==14:
            card = 'A'
            cards.append(card)
        elif value==13:
            card = 'K'
            cards.append(card)
        elif value==12:
            card = 'Q'
            cards.append(card)
        elif value==11:
            card = 'J'
            cards.append(card)
        else:
            card = value
            cards.append(str(card))
    five_hand = []
    if has_five==True and inorder==True:
        for card in cards:
            five_hand.append(card + suit)
        return 9, five_hand
    else:
        return 0, possible




def four_of_a_kind(pool,hand):
    four_of_kind = []
    Ace=[]
    King=[]
    Queen=[]
    Jack=[]
    Ten=[]
    Nine=[]
    Eight=[]
    Seven=[]
    Six=[]
    Five=[]
    Four=[]
    Three=[]
    Two=[]

    possible = pool + hand

    for card in possible:
        if card[0]=='A':
                Ace.append(card)
        if card[0]=='K':
                King.append(card)
        if card[0]=='Q':
                Queen.append(card)
        if card[0]=='J':
                Jack.append(card)
        if len(card)==3:
                Ten.append(card)
        if card[0]=='9':
                Nine.append(card)
        if card[0]=='8':
                Eight.append(card)
        if card[0]=='7':
                Seven.append(card)	
        if card[0]=='6':
                Six.append(card)
        if card[0]=='5':
                Five.append(card)
        if card[0]=='4':
                Four.append(card)
        if card[0]=='3':
                Three.append(card)
        if card[0]=='2':
                Two.append(card)

    if len(Ace) == 4:
        for card in Ace:
            four_of_kind.append(card)
    elif len(King) >= 4:
        for card in King:
            four_of_kind.append(card)
    elif len(Queen) == 4:
        for card in Queen:
            four_of_kind.append(card)
    elif len(Jack) == 4:
        for card in Jack:
            four_of_kind.append(card)
    elif len(Ten) == 4:
        for card in Ten:
            four_of_kind.append(card)
    elif len(Nine) == 4:
        for card in Nine:
            four_of_kind.append(card)
    elif len(Eight) == 4:
        for card in Eight:
            four_of_kind.append(card)
    elif len(Seven) == 4:
        for card in Seven:
            four_of_kind.append(card)
    elif len(Six) == 4:
        for card in Six:
            four_of_kind.append(card)
    elif len(Five) == 4:
        for card in Five:
            four_of_kind.append(card)
    elif len(Four) == 4:
        for card in Four:
            four_of_kind.append(card)
    elif len(Three) == 4:
        for card in Three:
            four_of_kind.append(card)
    elif len(Two) == 4:
        for card in Two:
            four_of_kind.append(card)

    if len(four_of_kind) == 4:
        left = possible
        for card in four_of_kind:
            left.remove(card)
        high_card = left[0]

        for card in left:
            if card[0] == 'A':
                high_card = card
            elif card[0] == 'K':
                high_card = card
            elif card[0] == 'Q':
                high_card = card
            elif card[0] == 'J':
                high_card = card
            else:
                try:
                    if int(card[-3:-1]) >= int(high_card[-3:-1]):
                        high_card = card
                except ValueError:
                    high_card = high_card
        five_hand = four_of_kind + [high_card]
        return 8, five_hand
    else:
        return 0, []

def full_house(pool,hand):
    three_of_kind = []
    pair = []
    Ace=[]
    King=[]
    Queen=[]
    Jack=[]
    Ten=[]
    Nine=[]
    Eight=[]
    Seven=[]
    Six=[]
    Five=[]
    Four=[]
    Three=[]
    Two=[]

    possible = pool + hand

    for card in possible:
        if card[0]=='A':
            Ace.append(card)
        if card[0]=='K':
            King.append(card)
        if card[0]=='Q':
            Queen.append(card)
        if card[0]=='J':
            Jack.append(card)
        if len(card)==3:
            Ten.append(card)
        if card[0]=='9':
            Nine.append(card)
        if card[0]=='8':
            Eight.append(card)
        if card[0]=='7':
            Seven.append(card)	
        if card[0]=='6':
            Six.append(card)
        if card[0]=='5':
            Five.append(card)
        if card[0]=='4':
            Four.append(card)
        if card[0]=='3':
            Three.append(card)
        if card[0]=='2':
            Two.append(card)

    if len(Ace) == 3:
        for card in Ace:
            three_of_kind.append(card)
    elif len(King) == 3:
        for card in King:
            three_of_kind.append(card)
    elif len(Queen) == 3:
        for card in Queen:
            three_of_kind.append(card)
    elif len(Jack) == 3:
        for card in Jack:
            three_of_kind.append(card)
    elif len(Ten) == 3:
        for card in Ten:
            three_of_kind.append(card)
    elif len(Nine) == 3:
        for card in Nine:
            three_of_kind.append(card)
    elif len(Eight) == 3:
        for card in Eight:
            three_of_kind.append(card)
    elif len(Seven) == 3:
        for card in Seven:
            three_of_kind.append(card)
    elif len(Six) == 3:
        for card in Six:
            three_of_kind.append(card)
    elif len(Five) == 3:
        for card in Five:
            three_of_kind.append(card)
    elif len(Four) == 3:
        for card in Four:
            three_of_kind.append(card)
    elif len(Three) == 3:
        for card in Three:
            three_of_kind.append(card)
    elif len(Two) == 3:
        for card in Two:
            three_of_kind.append(card)

    if len(Ace) >= 2:
        if Ace == three_of_kind:
            pass
        else:
            pair.append(Ace[0])
            pair.append(Ace[1])
    if len(King) >= 2:
        if King == three_of_kind:
            pass
        else:
            pair.append(King[0])
            pair.append(King[1])
    if len(Queen) >= 2:
        if Queen == three_of_kind:
            pass
        else:
            pair.append(Queen[0])
            pair.append(Queen[1])
    if len(Jack) >= 2:
        if Jack == three_of_kind:
            pass
        else:
            pair.append(Jack[0])
            pair.append(Jack[1])
    if len(Ten) >= 2:
        if Ten == three_of_kind:
            pass
        else:
            pair.append(Ten[0])
            pair.append(Ten[1])
    if len(Nine) >= 2:
        if Nine == three_of_kind:
            pass
        else:
            pair.append(Nine[0])
            pair.append(Nine[1])
    if len(Eight) >= 2:
        if Eight == three_of_kind:
            pass
        else:
            pair.append(Eight[0])
            pair.append(Eight[1])
    if len(Seven) >= 2:
        if Seven == three_of_kind:
            pass
        else:
            pair.append(Seven[0])
            pair.append(Seven[1])
    if len(Six) >= 2:
        if Six == three_of_kind:
            pass
        else:
            pair.append(Six[0])
            pair.append(Six[1])
    if len(Five) >= 2:
        if Five == three_of_kind:
            pass
        else:
            pair.append(Five[0])
            pair.append(Five[1])
    if len(Four) >= 2:
        if Four == three_of_kind:
            pass
        else:
            pair.append(Four[0])
            pair.append(Four[1])
    if len(Three) >= 2:
        if Three == three_of_kind:
            pass
        else:
            pair.append(Three[0])
            pair.append(Three[1])
    if len(Two) >= 2:
        if Two == three_of_kind:
            pass
        else:
            pair.append(Two[0])
            pair.append(Two[1])

    if len(three_of_kind) == 3 and len(pair) == 2:
        five_hand = three_of_kind + pair
        return 7, five_hand
    else:
        return 0, possible



def flush(pool,hand):
    hearts  = []
    diamonds = []
    spades = []
    clubs = []
    inorder=False
    has_five=False
    possible = pool + hand
    for card in possible:
        if card[-1] == 'H':
            hearts.append(card)
        elif card [-1] == 'D':
            diamonds.append(card)
        elif card[-1] == 'S':
            spades.append(card)
        elif card[-1] == 'C':
            clubs.append(card)
    if len(hearts)>=5:
            return 6, hearts[0:5]
    elif len(diamonds)>=5:
            return 6, diamonds[0:5]
    elif len(clubs)>=5:
            return 6, clubs[0:5]
    elif len(spades)>=5:
            return 6, spades[0:5]
    else:
        return 0, possible



def straight(pool,hand):
    possible=pool+hand
	
    mylist=[]
    possible_values_rand = []
    
    for card in possible:
        if card[0]=='A':
                num=14
                num2=1
                mylist.append(num)
                mylist.append(num2)
                possible_values_rand.append(f'{num}{card[-1]}')
                possible_values_rand.append(f'{num2}{card[-1]}')
        elif card[0]=='K':
                num=13
                mylist.append(num)
                possible_values_rand.append(f'{num}{card[-1]}')
        elif card[0]=='Q':
                num=12
                mylist.append(num)
                possible_values_rand.append(f'{num}{card[-1]}')
        elif card[0]=='J':
                num=11
                mylist.append(num)
                possible_values_rand.append(f'{num}{card[-1]}')
        elif len(card)==3:
                num=10
                mylist.append(num)
                possible_values_rand.append(f'{num}{card[-1]}')
        else: 
                mylist.append(int(card[0]))
                possible_values_rand.append(card)

    mylist.sort()
    
    mylist_nodup = []
    
    for value in mylist:
        if value not in mylist_nodup:
            mylist_nodup.append(value)
    mylist = mylist_nodup

    five_hand = []
    go = True
    
    if len(mylist) < 5:
        return 0, five_hand
    if len(mylist) == 5:
        if mylist[1] == mylist[0]+1 and mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1:
            values = mylist
        else:
            go = False
    elif len(mylist) == 6:
        if mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1 and mylist[5] == mylist[4]+1:
            values = mylist[1:6]
        elif mylist[1] == mylist[0]+1 and mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1:
            values = mylist[0:5]
        else:
            go = False
    elif len(mylist) == 7:
        if mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1 and mylist[5] == mylist[4]+1 and mylist[6] == mylist[5]+1:
            values = mylist[2:7]
        elif mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1 and mylist[5] == mylist[4]+1:
            values = mylist[1:6]
        elif mylist[1] == mylist[0]+1 and mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1:
            values = mylist[0:5]
        else:
            go = False
    elif len(mylist) == 8:
        if mylist[4] == mylist[3]+1 and mylist[5] == mylist[4]+1 and mylist[6] == mylist[5]+1 and mylist[7] == mylist[6]+1:
            values = mylist[3:8]
        elif mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1 and mylist[5] == mylist[4]+1 and mylist[6] == mylist[5]+1:
            values = mylist[2:7]
        elif mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1 and mylist[5] == mylist[4]+1:
            values = mylist[1:6]
        elif mylist[1] == mylist[0]+1 and mylist[2] == mylist[1]+1 and mylist[3] == mylist[2]+1 and mylist[4] == mylist[3]+1:
            values = mylist[0:5]
        else:
            go = False

    
    if go != False:
        num_suits = []
        for value in values:
            prev_val = 0
            for card in possible_values_rand:
                if int(card[-3:-1]) == value:
                    if int(card[-3:-1]) != prev_val:
                        num_suits.append(card)
                        prev_val = int(card[-3:-1])
        cards = []
        for card in num_suits:
            if int(card[-3:-1])==14 or int(card[-3:-1]) == 1:
                cards.append(f'A{card[-1]}')
            elif int(card[-3:-1])==13:
                cards.append(f'K{card[-1]}')
            elif int(card[-3:-1])==12:
                cards.append(f'Q{card[-1]}')
            elif int(card[-3:-1])==11:
                cards.append(f'J{card[-1]}')
            else:
                cards.append(card)
            five_hand = cards
        return 5, five_hand
    else:
        return 0, five_hand


def three_of_a_kind(pool,hand):
    three_of_kind = []
    Ace=[]
    King=[]
    Queen=[]
    Jack=[]
    Ten=[]
    Nine=[]
    Eight=[]
    Seven=[]
    Six=[]
    Five=[]
    Four=[]
    Three=[]
    Two=[]

    possible = pool + hand

    for card in possible:
        if card[0]=='A':
                Ace.append(card)
        if card[0]=='K':
                King.append(card)
        if card[0]=='Q':
                Queen.append(card)
        if card[0]=='J':
                Jack.append(card)
        if len(card)==3:
                Ten.append(card)
        if card[0]=='9':
                Nine.append(card)
        if card[0]=='8':
                Eight.append(card)
        if card[0]=='7':
                Seven.append(card)	
        if card[0]=='6':
                Six.append(card)
        if card[0]=='5':
                Five.append(card)
        if card[0]=='4':
                Four.append(card)
        if card[0]=='3':
                Three.append(card)
        if card[0]=='2':
                Two.append(card)

    if len(Ace) == 3:
        three_of_kind = Ace
    elif len(King) == 3:
        three_of_kind = King
    elif len(Queen) == 3:
        three_of_kind = Queen
    elif len(Jack) == 3:
        three_of_kind = Jack
    elif len(Ten) == 3:
        three_of_kind = Ten
    elif len(Nine) == 3:
        three_of_kind = Nine
    elif len(Eight) == 3:
        three_of_kind = Eight
    elif len(Seven) == 3:
        three_of_kind = Seven
    elif len(Six) == 3:
        three_of_kind = Six
    elif len(Five) == 3:
        three_of_kind = Five
    elif len(Four) == 3:
        three_of_kind = Four
    elif len(Three) == 3:
        three_of_kind = Three
    elif len(Two) == 3:
        three_of_kind = Two

    if len(three_of_kind) == 3:
        five_hand = three_of_kind + ['0N','0N']
        left = possible
        for card in three_of_kind:
            left.remove(card)
        num_suits = []
        values = []
        for card in left:
            if card[0]=='A':
                num_suits.append(f'14{card[-1]}')
                values.append(14)
            elif card[0]=='K':
                num_suits.append(f'13{card[-1]}')
                values.append(13)
            elif card[0]=='Q':
                num_suits.append(f'12{card[-1]}')
                values.append(12)
            elif card[0]=='J':
                num_suits.append(f'11{card[-1]}')
                values.append(11)
            else: 
                num_suits.append(card)
                values.append(int(card[-3:1]))
        values.sort()
        val1 = values[-1]
        val2 = values[-2]
        for card in num_suits:
            if int(card[-3:-1]) == val1:
                append = True
                pos = 3
            elif int(card[-3:-1]) == val2:
                append = True
                pos = 4
            else:
                append = False
            if append == True:
                if card[-3:-1]=='14':
                    five_hand[pos] = (f'A{card[-1]}')
                elif card[-3:-1]=='13':
                    five_hand[pos] = (f'K{card[-1]}')
                elif card[-3:-1]=='12':
                    five_hand[pos] = (f'Q{card[-1]}')
                elif card[-3:-1]=='11':
                    five_hand[pos] = (f'J{card[-1]}')
                else: 
                    five_hand[pos] = (card)
                    
        return 4, five_hand
    else:
        return 0, []
    
def two_pair(pool,hand):
    pair = []
    Ace=[]
    King=[]
    Queen=[]
    Jack=[]
    Ten=[]
    Nine=[]
    Eight=[]
    Seven=[]
    Six=[]
    Five=[]
    Four=[]
    Three=[]
    Two=[]

    possible = pool + hand

    for card in possible:
        if card[0]=='A':
                Ace.append(card)
        if card[0]=='K':
                King.append(card)
        if card[0]=='Q':
                Queen.append(card)
        if card[0]=='J':
                Jack.append(card)
        if len(card)==3:
                Ten.append(card)
        if card[0]=='9':
                Nine.append(card)
        if card[0]=='8':
                Eight.append(card)
        if card[0]=='7':
                Seven.append(card)	
        if card[0]=='6':
                Six.append(card)
        if card[0]=='5':
                Five.append(card)
        if card[0]=='4':
                Four.append(card)
        if card[0]=='3':
                Three.append(card)
        if card[0]=='2':
                Two.append(card)

    if len(Ace) >= 2:
        pair.append(Ace[0])
        pair.append(Ace[1])
    if len(King) >= 2:
        pair.append(King[0])
        pair.append(King[1])
    if len(Queen) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Queen[0])
            pair.append(Queen[1])
    if len(Jack) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Jack[0])
            pair.append(Jack[1])
    if len(Ten) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Ten[0])
            pair.append(Ten[1])
    if len(Nine) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Nine[0])
            pair.append(Nine[1])
    if len(Eight) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Eight[0])
            pair.append(Eight[1])
    if len(Seven) >= 2:
        if len(pair) >= 4:
                pass
        else:
            pair.append(Seven[0])
            pair.append(Seven[1])
    if len(Six) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Six[0])
            pair.append(Six[1])
    if len(Five) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Five[0])
            pair.append(Five[1])
    if len(Four) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Four[0])
            pair.append(Four[1])
    if len(Three) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Three[0])
            pair.append(Three[1])
    if len(Two) >= 2:
        if len(pair) >= 4:
            pass
        else:
            pair.append(Two[0])
            pair.append(Two[1])
            
    if len(pair) == 4:
        five_hand = pair
        left = possible
        for card in pair:
            left.remove(card)
        num_suits = []
        values = []
        for card in left:
            if card[0]=='A':
                num_suits.append(f'14{card[-1]}')
                values.append(14)
            elif card[0]=='K':
                num_suits.append(f'13{card[-1]}')
                values.append(13)
            elif card[0]=='Q':
                num_suits.append(f'12{card[-1]}')
                values.append(12)
            elif card[0]=='J':
                num_suits.append(f'11{card[-1]}')
                values.append(11)
            else: 
                num_suits.append(card)
                values.append(int(card[-3:1]))
        values.sort()
        
        for card in num_suits:
            if len(pair) < 5:
                if int(card[-3:-1]) == values[-1]:
                    if card[-3:-1]=='14':
                        five_hand.append(f'A{card[-1]}')
                    elif card[-3:-1]=='13':
                        five_hand.append(f'K{card[-1]}')
                    elif card[-3:-1]=='12':
                        five_hand.append(f'Q{card[-1]}')
                    elif card[-3:-1]=='11':
                        five_hand.append(f'J{card[-1]}')
                    else: 
                        five_hand.append(card)
        return 3, five_hand
    else:
        return 0, possible
    
def pair(pool,hand):
    pair = []
    Ace=[]
    King=[]
    Queen=[]
    Jack=[]
    Ten=[]
    Nine=[]
    Eight=[]
    Seven=[]
    Six=[]
    Five=[]
    Four=[]
    Three=[]
    Two=[]

    possible = pool + hand

    for card in possible:
        if card[0]=='A':
                Ace.append(card)
        if card[0]=='K':
                King.append(card)
        if card[0]=='Q':
                Queen.append(card)
        if card[0]=='J':
                Jack.append(card)
        if len(card)==3:
                Ten.append(card)
        if card[0]=='9':
                Nine.append(card)
        if card[0]=='8':
                Eight.append(card)
        if card[0]=='7':
                Seven.append(card)	
        if card[0]=='6':
                Six.append(card)
        if card[0]=='5':
                Five.append(card)
        if card[0]=='4':
                Four.append(card)
        if card[0]=='3':
                Three.append(card)
        if card[0]=='2':
                Two.append(card)

    if len(Ace) >= 2:
        pair.append(Ace[0])
        pair.append(Ace[1])
    elif len(King) >= 2:
        pair.append(King[0])
        pair.append(King[1])
    elif len(Queen) >= 2:
        pair.append(Queen[0])
        pair.append(Queen[1])
    elif len(Jack) >= 2:
        pair.append(Jack[0])
        pair.append(Jack[1])
    elif len(Ten) >= 2:
        pair.append(Ten[0])
        pair.append(Ten[1])
    elif len(Nine) >= 2:
        pair.append(Nine[0])
        pair.append(Nine[1])
    elif len(Eight) >= 2:
        pair.append(Eight[0])
        pair.append(Eight[1])
    elif len(Seven) >= 2:
        pair.append(Seven[0])
        pair.append(Seven[1])
    elif len(Six) >= 2:
        pair.append(Six[0])
        pair.append(Six[1])
    elif len(Five) >= 2:
        pair.append(Five[0])
        pair.append(Five[1])
    elif len(Four) >= 2:
        pair.append(Four[0])
        pair.append(Four[1])
    elif len(Three) >= 2:
        pair.append(Three[0])
        pair.append(Three[1])
    elif len(Two) >= 2:
        pair.append(Two[0])
        pair.append(Two[1])

    if len(pair) == 2:
        five_hand = pair + ['0N','0N','0N']
        left = possible
        for card in pair:
            left.remove(card)

        num_suits = []
        values = []
        for card in left:
            if card[0]=='A':
                num_suits.append(f'14{card[-1]}')
                values.append(14)
            elif card[0]=='K':
                num_suits.append(f'13{card[-1]}')
                values.append(13)
            elif card[0]=='Q':
                num_suits.append(f'12{card[-1]}')
                values.append(12)
            elif card[0]=='J':
                num_suits.append(f'11{card[-1]}')
                values.append(11)
            else: 
                num_suits.append(card)
                values.append(int(card[-3:-1]))
        values.sort()
        val1 = values[-1]
        val2 = values[-2]
        val3 = values[-3]
        for card in num_suits:
            if int(card[-3:-1]) == val1:
                append = True
                pos = 2
            elif int(card[-3:-1]) == val2:
                append = True
                pos = 3
            elif int(card[-3:-1]) == val3:
                append = True
                pos = 4
            else:
                append = False
            if append == True:
                if (card[-3:-1])=='14':
                    five_hand[pos] = (f'A{card[-1]}')
                elif card[-3:-1]=='13':
                    five_hand[pos] = (f'K{card[-1]}')
                elif card[-3:-1]=='12':
                    five_hand[pos] = (f'Q{card[-1]}')
                elif card[-3:-1]=='11':
                    five_hand[pos] = (f'J{card[-1]}')
                else: 
                    five_hand[pos] = (card)
        return 2, five_hand
    else:
        return 0, []



def high_card(pool, hand):
    possible = pool+hand

    five_hand = ['0N','0N','0N','0N','0N']

    num_suits = []
    values = []
    for card in possible:
        if card[0]=='A':
            num_suits.append(f'14{card[-1]}')
            values.append(14)
        elif card[0]=='K':
            num_suits.append(f'13{card[-1]}')
            values.append(13)
        elif card[0]=='Q':
            num_suits.append(f'12{card[-1]}')
            values.append(12)
        elif card[0]=='J':
            num_suits.append(f'11{card[-1]}')
            values.append(11)
        else: 
            num_suits.append(card)
            values.append(int(card[-3:-1]))
    values.sort()
    val1 = values[-1]
    val2 = values[-2]
    val3 = values[-3]
    val4 = values[-4]
    val5 = values[-5]
    for card in num_suits:
        if int(card[-3:-1]) == val1:
            append = True
            pos = 0
        elif int(card[-3:-1]) == val2:
            append = True
            pos = 1
        elif int(card[-3:-1]) == val3:
            append = True
            pos = 2
        elif int(card[-3:-1]) == val4:
            append = True
            pos = 3
        elif int(card[-3:-1]) == val5:
            append = True
            pos = 4
        else:
            append = False
        if append == True:
            if card[-3:-1]=='14':
                five_hand[pos] = (f'A{card[-1]}')
            elif card[-3:-1]=='13':
                five_hand[pos] = (f'K{card[-1]}')
            elif card[-3:-1]=='12':
                five_hand[pos] = (f'Q{card[-1]}')
            elif card[-3:-1]=='11':
                five_hand[pos] = (f'J{card[-1]}')
            else: 
                five_hand[pos] = (card)
    return 1, five_hand
        
        
    
    
main()















