import random
from art import logo

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 11 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if c_score == u_score:
        return "draw."
    elif c_score == 0:
        return "lose, opponent has blackjack."
    elif u_score == 0:
        return "win with a blackjack."
    elif u_score > 21:
        return "You went over. you lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and Current Score = {user_score}")
        print(f"Computer card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to draw another card? Type 'y' or 'n'.").lower()
            if another_card == 'y':
                user_cards.append(deal_cards())
                print(user_cards)
                print(calculate_score(user_cards))
            else:
                is_game_over = True
                print("Game over.")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ") == 'y':
    print("\n" * 20)
    play_game()
