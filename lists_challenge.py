import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    play = input('Press enter to pick a card press "Q" to quit')
    if play == "q":
        print("Goodbye")
        break
    elif play != "q":
        card = random.choice(diamonds)
        diamonds.remove(card)
        hand.append(card)
        print("You hand: ", card)

if not diamonds:
    print("There are no more cards to pick.")
