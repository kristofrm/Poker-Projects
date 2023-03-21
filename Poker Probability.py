import random

def main():
    print('Calculating hand probabilities...\n')
    
    #Royal Flush
    desired = 10
    avg_tries, percent = probability(desired, royal_flush)
    print('Royal Flush:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Straight Flush
    desired = 9
    avg_tries, percent = probability(desired, straight_flush)
    print('Straight Flush:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Four of a Kind
    desired = 8
    avg_tries, percent = probability(desired, four_of_a_kind)
    print('Four of a Kind:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Full House
    desired = 7
    avg_tries, percent = probability(desired, full_house)
    print('Full House:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Flush
    desired = 6
    avg_tries, percent = probability(desired, flush)
    print('Flush:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Straight
    desired = 5
    avg_tries, percent = probability(desired, straight)
    print('Straight:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Three of a Kind
    desired = 4
    avg_tries, percent = probability(desired, three_of_a_kind)
    print('Three of a Kind:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Two Pair
    desired = 3
    avg_tries, percent = probability(desired, two_pair)
    print('Two Pair:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #Pair
    desired = 2
    avg_tries, percent = probability(desired, pair)
    print('Pair:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

    #High Card
    desired = 1
    avg_tries, percent = probability(desired, high_card)
    print('High Card:')
    print(f'Average number of tries: {avg_tries}')
    print(f'Percent chance: {percent:.5}%\n')

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

def probability(desired, function):
    result = 0
    count = 0
    total_tries = 0
    n = 1000
    for i in range(n):
        while result != desired:
            deck_dictionary = deck()
            hand = []
            for i in range(2):
                card, deck_dictionary = deal_card(deck_dictionary)
                hand.append(card)
            pool = []
            for i in range(5):
                card, deck_dictionary = deal_card(deck_dictionary)
                pool.append(card)
            result, five_hand = function(pool, hand)
            count += 1
        total_tries += count
        result = 0
        count = 0
    avg_tries = total_tries/n
    percent = 100*(1/(total_tries/n))
    return avg_tries, percent

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
        return 0, []


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
        return 0, []


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
        
