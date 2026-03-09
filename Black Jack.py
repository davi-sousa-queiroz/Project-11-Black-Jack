# ---------- IMPORTS -----------
import random
# ------- GAME VARIABLES ---------
deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]

player_hand = []
dealer_hand = []
# ---------- FUNCTIONS -----------
def draw_card():
    return random.choice(deck)
def calculate_score(hand):
    return sum(hand)
def show_hands(player, dealer):
    print("Your hand:", player)
    print("Dealer hand:", dealer)
def dealer_turn():
    global dealer_hand
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card())
def determine_winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score > 21:
        print('You busted! Dealer wins!')

    elif dealer_score > 21:
        print('Dealer busted! You win!')

    elif player_score > dealer_score:
        print('You win!')

    elif dealer_score > player_score:
        print('Dealer wins!')

    else:
        print('It\'s a tie!')
# --------- BLACK JACK -----------
while True:
        player_hand = []
        dealer_hand = []

        player_hand.append(draw_card())
        player_hand.append(draw_card())

        dealer_hand.append(draw_card())
        dealer_hand.append(draw_card())

        show_hands(player_hand, dealer_hand)

        while sum(player_hand) < 21:
            choice = input('Hit or Stand?').lower()

            if choice == 'hit':
                player_hand.append(draw_card())
                print('Your hand:', player_hand)

            elif choice == 'stand':
                break

        dealer_turn()
        show_hands(player_hand, dealer_hand)
        determine_winner(player_hand, dealer_hand)

        again = input('Do you want to play again?').lower()
        if again[0] == 'no':
            print('Thanks for playing!')
            break