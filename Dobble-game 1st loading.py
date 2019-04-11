"""
  BUG FIXING - NOTE:
  ***NOTE****
 Deleting the symbol once it is entried in the card, as it might result to a bug as there is a possibility of selecting the same symbol by random.choice() function..
"""

import string
import random

symbols = []
symbols = list(string.ascii_letters)
# Creating a card with minimum 5 symbols
card1 = [0]*5
card2 = [0]*5

# Picking a random position (1..5) for placing a same symbol in both card1 and card2
pos1 = random.randint(0, 4)  # pos1 for card-1
pos2 = random.randint(0, 4)  # pos2 for card-2

# Picking a random symbol from a list of 52 values (26-lower, 26-upper)
samesymbol = random.choice(symbols)
symbols.remove(samesymbol)  # ***NOTE***
# placing the randomly  selected in the 2 cards
if pos1 == pos2:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    # Observe carefully near the index values of the cards, they are interchanged to card-1 and card-2 positions because the samesymbol which is selected is already placed at that index
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
# so now, 1 same symbol is placed in both the cards, now its time to place some other random symbols in leftover positions in both the cards

i = 0
while i < 5:
    if i != pos1 and i != pos2:  # this is because we would not like to replace the already placed symbol(same symbol that is placed already in both the cards)
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)  # Refer ***NOTE****
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)   # Refer ***NOTE***

        # Now placing the randomly selected symbols in the cards
        card1[i] = alphabet1
        card2[i] = alphabet2

        # Iteration of the loop
    i += 1

print("Card 1 : ", card1)
print("Card 2 : ", card2)

userchoice = input("Select the similar Letter : ")
if userchoice == samesymbol:
    print("You WON !!!")
else:
    print("You lost, Please try again!!")

