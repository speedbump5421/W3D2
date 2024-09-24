
import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    user_choice = input(
        "Press Enter to pick a card, or press q then Enter to quit: ")
    if user_choice.lower() == 'q':
        exit()
    elif user_choice == '':
        card = random.choice(diamonds)
        hand.append(card)
        diamonds.remove(card)
        print("\nYou picked", card, "which has been added to your hand.")
        print("Your hand:", hand)
        print("Remaining deck:", diamonds, "\n")
    else:
        print("Invalid input. Please read the instructions this time.")

if not diamonds:
    print("There are no more cards to draw. Game over.\n")
    exit()
