import random

def shuffle():
    global player_card, dealer_card, deck
    ranks = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ["SPADE", "HEART", "DIAMOND", "CLUB"]
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    player_card = deck[:2]
    dealer_card = deck[2:4]
    deck = deck[4:]

def compute_value(cards):
    value = 0
    ace_count = 0
    for card in cards:
        if card['rank'] == 'ACE':
            value += 11
            ace_count += 1
        elif card['rank'] in ['J', 'Q', 'K']:
            value += 10
        else:
            value += int(card['rank'])
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value

def again():
    return input("\nWant to play again? (y/n): ").lower() == 'y'

def play():
    shuffle()
    player_value = compute_value(player_card)
    if player_value == 21:
        print("\nPlayer's current value is Blackjack! (21)")
    else:
        print(f"\nPlayer's current value is {player_value}")
    print("with the hand:", ", ".join(f"{card['rank']}-{card['suit']}" for card in player_card))
    while True:
        if player_value > 21:
            print("\nYour current value is Bust! (>21)")
            print("with the hand:", ", ".join(f"{card['rank']}-{card['suit']}" for card in player_card))
            print("\n*** Dealer wins! ***")
            if again():
                play()
            return
        elif player_value == 21:
            print("\nPlayer has reached 21!")
            break
        choice = input("\nHit or stay? (Hit = 1, Stay = 0): ")
        if choice == '1':
            player_card.append(deck.pop())
            player_value = compute_value(player_card)
            print(f"You draw {player_card[-1]['rank']}-{player_card[-1]['suit']}")
            print(f"\nPlayer's current value is {player_value}")
            print("with the hand:", ", ".join(f"{card['rank']}-{card['suit']}" for card in player_card))
        else:
            break
    deal(player_value)  # Pass player_value as an argument

def deal(player_value):  # Accept player_value as an argument
    dealer_value = compute_value(dealer_card)
    print(f"\nDealer's current value is {dealer_value}")
    print("with the hand:", ", ".join(f"{card['rank']}-{card['suit']}" for card in dealer_card))
    while dealer_value < 17:
        dealer_card.append(deck.pop())
        dealer_value = compute_value(dealer_card)
        print(f"Dealer draws {dealer_card[-1]['rank']}-{dealer_card[-1]['suit']}")
    if dealer_value > 21:
        print("\nDealer's current value is Bust! (>21)")
        print("with the hand:", ", ".join(f"{card['rank']}-{card['suit']}" for card in dealer_card))
        print("\n*** You beat the dealer! ***")
    elif dealer_value > player_value:
        print("\n*** Dealer wins! ***")
    elif dealer_value < player_value:
        print("\n*** You beat the dealer! ***")
    else:
        print("\n*** You tied the dealer, nobody wins. ***")
    if again():
        play()

play()
