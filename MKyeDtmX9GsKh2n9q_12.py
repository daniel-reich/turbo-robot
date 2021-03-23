"""


Create a function that generates a poker deck.

A poker deck contains 52 cards in total, 13 cards for each of the four suits (
**♦** diamonds, **♠** clubs, **♥** hearts and **♣** spades) ranked **2, 3, 4,
5, 6, 7, 8, 9, 10, J, Q, K, A**.

Your function should return a **list** (deck) containing each card as a
**tuple** in the following format:

    (rank, suit)

Where _rank_ is a number from 2 to 14 (11, 12, 13 & 14 being J, Q, K & A
respectively) and _suit_ is a string with the first letter of the the card's
suit ("d", "c", "h" & "s" for diamonds, clubs, hearts & spades respectively).

### Examples

    Five of hearts ➞ (5, "h")
    
    Queen of Spades ➞ (12, "s")
    
    Ace of Clubs ➞ (14, "c")

### Notes

Extra points for shuffling the deck.

"""

def gen_deck():
    deck = []
    suits = ["d","h","c","s"]
    rank = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    for a in suits:
        for b in rank:
            deck.append(tuple([b,a]))
    return(deck)

