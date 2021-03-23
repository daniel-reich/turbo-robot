"""


Create a function that takes in two lists and determines whether there exists
a flush.

  * The first list represents the 5 cards dealt on the table.
  * The second list represents the 2 cards in your hand.

Notation: card number and suit (abbreviated as S = Spades, H = Hearts, D =
Diamonds, C = Clubs) separated by an underscore.

### Examples

    check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) ➞ True // diamond flush
    
    check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) ➞ True // spade flush
    
    check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) ➞ False

### Notes

Hint: If there aren't at least 3 cards of the same suit on the table, there is
zero chance of there being a flush.

"""

def check_flush(table, hand):
    Spades = []
    Hearts = []
    Diamonds = []
    Clubs = []
    table.append(cards for cards in hand)
    for cards in table:
        for card in cards:
            if card[-1] == "S":
                Spades.append(card)
            if card[-1] == "H":
                Hearts.append(card)
            if card[-1] == "D":
                Diamonds.append(card)
            if card[-1] == "C":
                Clubs.append(card)
                
    if len(Spades) >= 5 or len(Hearts) >= 5 or len(Diamonds) >= 5 or len(Clubs) >= 5:
        return True
    else:
        return False

