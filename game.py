import random
import os


class Card:
    def __init__(self, card_face, value, symbol):
        self.card_face = card_face
        self.value = value
        self.symbol = symbol


def clear_screen():
    # Clear screen for Windows and Unix-like systems
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/Mac


def show_cards(cards, hidden):
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card.card_face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|  {}             |'.format(card.card_face)
        elif card.value == 10:
            s = s + '\t|  {}            |'.format(card.value)
        else:
            s = s + '\t|  {}             |'.format(card.value)

    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|      * *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|    *     *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|       {}        |'.format(card.symbol)
    if hidden:
        s += '\t|          *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|         *      |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card.card_face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|            {}   |'.format(card.card_face)
        elif card.value == 10:
            s = s + '\t|           {}   |'.format(card.value)
        else:
            s = s + '\t|            {}   |'.format(card.value)
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|________________|'
    if hidden:
        s += '\t|________________|'
    print(s)
    print()


def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck


def play_blackjack(deck):
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    clear_screen()

    # Initial deal
    while len(player_cards) < 2:
        player_card, deck = deal_card(deck)
        player_cards.append(player_card)
        player_score += player_card.value

        # Adjust score if both cards are Aces
        if len(player_cards) == 2 and player_cards[0].value == 11 and player_cards[1].value == 11:
            player_cards[0].value = 1
            player_score -= 10

        print('PLAYER CARDS: ')
        show_cards(player_cards, False)
        print('PLAYER SCORE = ', player_score)

        input('Continue...')

        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

        # Adjust score if both dealer cards are Aces
        if len(dealer_cards) == 2 and dealer_cards[0].value == 11 and dealer_cards[1].value == 11:
            dealer_cards[1].value = 1
            dealer_score -= 10

        print('DEALER CARDS: ')
        if len(dealer_cards) == 1:
            show_cards(dealer_cards, False)
            print('DEALER SCORE = ', dealer_score)
        else:
            show_cards(dealer_cards[:-1], True)
            print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)

        input('Continue...')

    if player_score == 21:
        print('PLAYER HAS A BLACKJACK!!!!')
        print('PLAYER WINS!!!!')
        return

    clear_screen()
    print('DEALER CARDS: ')
    show_cards(dealer_cards[:-1], True)
    print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)
    print()
    print('PLAYER CARDS: ')
    show_cards(player_cards, False)
    print('PLAYER SCORE = ', player_score)

    # Player's turn
    while player_score < 21:
        choice = input('Enter H to Hit or S to Stand: ').upper()
        if choice not in ['H', 'S']:
            clear_screen()
            print('Invalid choice!! Try Again...')
            continue

        if choice == 'S':
            break
        else:
            player_card, deck = deal_card(deck)
            player_cards.append(player_card)
            player_score += player_card.value

            # Adjust score if any Aces present
            card_pos = 0
            while player_score > 21 and card_pos < len(player_cards):
                if player_cards[card_pos].value == 11:
                    player_cards[card_pos].value = 1
                    player_score -= 10
                card_pos += 1

            if player_score > 21:
                break

            clear_screen()
            print('DEALER CARDS: ')
            show_cards(dealer_cards[:-1], True)
            print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)
            print()
            print('PLAYER CARDS: ')
            show_cards(player_cards, False)
            print('PLAYER SCORE = ', player_score)

    # Dealer's turn
    clear_screen()
    print('PLAYER CARDS: ')
    show_cards(player_cards, False)
    print('PLAYER SCORE = ', player_score)
    print()
    print('DEALER IS REVEALING THEIR CARDS....')
    show_cards(dealer_cards, False)
    print('DEALER SCORE = ', dealer_score)

    if player_score == 21:
        print('PLAYER HAS A BLACKJACK, PLAYER WINS!!!')
        return

    if player_score > 21:
        print('PLAYER BUSTED!!! GAME OVER!!!')
        return

    input('Continue...')
    while dealer_score < 17:
        clear_screen()
        print('DEALER DECIDES TO HIT.....')
        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

        # Adjust score if any Aces present
        card_pos = 0
        while dealer_score > 21 and card_pos < len(dealer_cards):
            if dealer_cards[card_pos].value == 11:
                dealer_cards[card_pos].value = 1
                dealer_score -= 10
            card_pos += 1

        print('PLAYER CARDS: ')
        show_cards(player_cards, False)
        print('PLAYER SCORE = ', player_score)
        print()
        print('DEALER CARDS: ')
        show_cards(dealer_cards, False)
        print('DEALER SCORE = ', dealer_score)
        if dealer_score > 21:
            break
        input('Continue...')

    # Final result
    if dealer_score > 21:
        print('DEALER BUSTED! YOU WIN!')
    elif dealer_score == 21:
        print('DEALER HAS A BLACKJACK! PLAYER LOSES')
    elif dealer_score == player_score:
        print('Push')
    elif player_score > dealer_score:
        print('PLAYER WINS')
    else:
        print('DEALER WINS')


def init_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    # UNICODE symbols for the suits
    suit_symbols = {'Spades': '\u2660', 'Hearts': '\u2665', 'Clubs': '\u2663', 'Diamonds': '\u2666'}
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []

    for suit in suits:
        for card in cards:
            if card in ['J', 'Q', 'K']:
                value = 10
            elif card == 'A':
                value = 11
            else:
                value = int(card)
            deck.append(Card(card, value, suit_symbols[suit]))

    return deck


def main():
    while True:
        deck = init_deck()
        play_blackjack(deck)
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!😘")
            break


if __name__ == "__main__":
    main()
