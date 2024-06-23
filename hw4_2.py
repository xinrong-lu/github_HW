import random

def shuffle(): #洗牌函數
    global player_card, dealer_card, deck
    ranks = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ["SPADE", "HEART", "DIAMOND", "CLUB"]
    deck = []
    for suit in suits: #組52張牌
        for rank in ranks:
            deck.append([suit, rank])
    random.shuffle(deck) #打亂
    player_card = []
    dealer_card = []
    for i in range(2): #每人拿兩張
        player_card.append(deck.pop())
        dealer_card.append(deck.pop())

def compute_value(cards): #算手上點數
    value = 0
    Ace = 0
    for card in cards:
        if card[1] == "ACE": #拿到ACE先算11點
            value += 11
            Ace += 1
        elif card[1] == "J" or card[1] == "Q" or card[1] == "K": #JQK 10點
            value += 10
        else:
            value += int(card[1]) #數字牌
    while Ace:
        if value > 21: #手上有ACE牌且點數大於21點 將ACE算為1
            value -= 10
            Ace -= 1
        else:
            break
    return value

def again(): #重來函數
    again = input("\n Want to play again? (y/n):")
    print()
    if again == "y":
        print("\n-------------------------------------")
        return True
    elif again == "n":
        return False
def play(): #玩家函數
    global player_value
    shuffle()
    stay = False
    while not stay:
        player_value = compute_value(player_card) #計算玩家點數
        if player_value > 21: #爆開
            print("Your current value is Bust! (>21)")
            print("with the hand: ", end="")
            for i in range(len(player_card)-1): #印出手上的牌
                print(player_card[i][1] + "-" + player_card[i][0] + ",", end=" ")
            print(player_card[len(player_card)-1][1] + "-" + player_card[len(player_card)-1][0])
            print("\n*** Dealer wins! ***") #莊家贏
            if again():
                play()
            else:
                break
            return
        else:
            if player_value == 21:
                print("\nPlayer's current value is Blackjack! (21)")
            else:
                print("\nPlayer's current value is %d" % player_value)
            print("with the hand: ", end="")
            for i in range(len(player_card)-1):
                print(player_card[i][1] + "-" + player_card[i][0] + ",", end=" ")
            print(player_card[len(player_card)-1][1] + "-" + player_card[len(player_card)-1][0])
            stay = not bool(int(input("\nHit or stay? (Hit = 1, Stay = 0):")))
            if not stay:    
                draw = deck.pop() #Hit則多拿一張牌
                player_card.append(draw)
                print("You draw " + draw[1] + "-" + draw[0])
                print()
            else: #Stay則換莊家
                deal()

def deal(): #莊家函數
    while True:
        dealer_value = compute_value(dealer_card)#計算莊家點數
        if dealer_value > 21: #爆開
            print("Dealer's current value is Bust! (>21)")
            print("with the hand: ", end="")
            for i in range(len(dealer_card)-1): #印出手上的牌
                print(dealer_card[i][1] + "-" + dealer_card[i][0] + ",", end=" ")
            print(dealer_card[len(dealer_card)-1][1] + "-" + dealer_card[len(dealer_card)-1][0])
            print("\n*** You bet the dealer! ***") #玩家贏
            if again():
                play()
            else:
                break
            return
        else:
            if dealer_value == 21:
                print("\nDealer's current value is Blackjack! (21)")
            else:
                print("\nDealer's current value is %d" % dealer_value)
            print("with the hand: ", end="")
            for i in range(len(dealer_card)-1):
                print(dealer_card[i][1] + "-" + dealer_card[i][0] + ",", end=" ")
            print(dealer_card[len(dealer_card)-1][1] + "-" + dealer_card[len(dealer_card)-1][0])
            if dealer_value < 17: #莊家少於17點必須抽牌    
                draw = deck.pop()
                dealer_card.append(draw)
                print("\nDealer draws " + draw[1] + "-" + draw[0])
            elif player_value > dealer_value: #玩家點數大於莊家點數
                print("\n*** You bet the dealer! ***") #玩家贏
                if again():
                    play()
                else:
                    break
                return
            elif player_value < dealer_value: #玩家點數小於莊家點數
                print("\n*** Dealer wins! ***") #莊家贏
                if again():
                    play()
                else:
                    break
                return
            elif player_value == dealer_value: #玩家點數等於莊家點數
                print("\n*** You tied the dealer, nobody wins. ***") #平手
                if again():
                    play()
                else:
                    break
                return
                
play()
