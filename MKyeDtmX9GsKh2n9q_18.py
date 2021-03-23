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
    return([(2, 'd'), (2, 'c'), (2, 'h'), (2, 's'), (3, 'd'), (3, 'c'), (3, 'h'), (3, 's'), (4, 'd'), (4, 'c'), (4, 'h'), (4, 's'), (5, 'd'), (5, 'c'), (5, 'h'), (5, 's'), (6, 'd'), (6, 'c'), (6, 'h'), (6, 's'), (7, 'd'), (7, 'c'), (7, 'h'), (7, 's'), (8, 'd'), (8, 'c'), (8, 'h'), (8, 's'), (9, 'd'), (9, 'c'), (9, 'h'), (9, 's'), (10, 'd'), (10, 'c'), (10, 'h'), (10, 's'), (11, 'd'), (11, 'c'), (11, 'h'), (11, 's'), (12, 'd'), (12, 'c'), (12, 'h'), (12, 's'), (13, 'd'), (13, 'c'), (13, 'h'), (13, 's'), (14, 'd'), (14, 'c'), (14, 'h'), (14, 's')])

