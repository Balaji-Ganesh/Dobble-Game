"""
Developed on 11th April, Thursday in 2019

This game is improved with the previous version by adding the difficulty level in choosing the letters

Difficulty level-1: only lowercase letters with the card size 5
Difficulty level-2: lowercase and uppercase letters with the card size 5
Difficulty level-3: lowercase and uppercase letters with the card size 8
Difficulty level-4: lowercase and uppercase letters with the card size 12
Difficulty level-5: lowercase and uppercase letters with the card size 15
"""

import string
import random
print("\n\t\t\t\t\"Welcome to the DOBBLE GAME\"\n")
print("Select the Difficulty level :")
print("\tLEVEL 1"); print("\tLEVEL 2"); print("\tLEVEL 3"); print("\tLEVEL 4"); print("\tLEVEL 5")
difflvl = int(input("Enter the difficulty level number : "))  # difflvl = difficultylevel
symbols = []
limit = 0  # Defines the number of symbols based on selected difficulty level
if difflvl == 1:
    symbols = list(string.ascii_lowercase)
    limit = 5
elif difflvl == 2:
    symbols = list(string.ascii_letters)
    limit = 5
elif difflvl == 3:
    symbols = list(string.ascii_letters)
    limit = 8
elif difflvl == 4:
    symbols = list(string.ascii_letters)
    limit = 12
elif difflvl == 5:
    symbols = list(string.ascii_letters)
    limit = 15

# Creating cards based on the difficulty level selected (as limit)
card1 = [0]*limit
card2 = [0]*limit

# Picking a random position (from 1..limit-1) for placing a same symbol in both card1 and card2
pos1 = random.randint(0, limit-1)  # pos1 for card-1
pos2 = random.randint(0, limit-1)  # pos2 for card-2

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
while i < limit:
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

userchoice = input("Select the similar Letter present in both cards : ")
if userchoice == samesymbol:
    print("Hurray You WON the game !!!")
else:
    print("You lost, Please try again!!")
    print("The letter is ", samesymbol)
    print("Present at {} in card-1 and at {} in card-2".format(pos1+1, pos2+2))
    for i in range(1, limit+1):
        print("  {}  ".format(i), end="")
    print()
    print(card1)
    print(card2)
    for i in range(1, limit+1):
        print("  {}  ".format(i), end="")

